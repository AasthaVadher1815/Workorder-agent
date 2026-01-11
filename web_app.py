"""
Work Order Agent - Excel Processor
Professional Web UI for processing work order changes with LLM

Upload Excel → Process with Master JSON Context → Get Results
"""

import os
import json
from pathlib import Path
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
from io import BytesIO
from excel.excel_parser import parse_excel_to_snapshot
from agent.orchestrator import process_input_snapshot
from database.connection import SessionLocal
from database.models.work_orders import WorkOrder

# Configuration
UPLOAD_FOLDER = 'uploads'
CONTEXT_FILE = 'data/work_orders_master.json'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

# Create Flask app
app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_master_json():
    """Load master JSON context."""
    try:
        with open(CONTEXT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading master JSON: {e}")
        return {}


def extract_qsid_context(master_data, qs_number):
    """Extract specific QS Number context from master JSON."""
    if not master_data or not qs_number:
        return None
    
    # Normalize search value
    search_qs = str(qs_number).strip().upper()
    
    # Search through all records in the JSON
    for query_key, records in master_data.items():
        if isinstance(records, list):
            for record in records:
                if isinstance(record, dict):
                    # Check multiple possible field names
                    qs = (
                        record.get("QS Number") or 
                        record.get("QS_Number") or 
                        record.get("QSNumber") or
                        record.get("qs_number") or
                        record.get("qsnumber")
                    )
                    
                    if qs:
                        record_qs = str(qs).strip().upper()
                        if record_qs == search_qs:
                            return record
    return None


@app.route('/')
def index():
    """Main page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and processing."""
    try:
        if 'excel_file' not in request.files:
            return jsonify({'error': 'No Excel file provided'}), 400
        
        excel_file = request.files['excel_file']
        model_name = request.form.get('model_name', 'gpt-4-mini')
        
        if not excel_file or not allowed_file(excel_file.filename):
            return jsonify({'error': 'Invalid file format. Use .xlsx or .xls'}), 400
        
        # Save uploaded file
        filename = secure_filename(excel_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        excel_file.save(filepath)
        
        # Parse Excel
        snap = parse_excel_to_snapshot(filepath)
        records = snap.get("records", [])
        
        if not records:
            os.remove(filepath)
            return jsonify({'error': 'Excel file is empty or invalid format'}), 400
        
        # Load master context
        master_json = load_master_json()
        
        # Extract work order from first record's QS Number (check all possible column names)
        first_record = records[0]
        first_qs = (
            first_record.get("QS Number") or 
            first_record.get("QS_Number") or 
            first_record.get("QSNumber") or
            first_record.get("qs_number") or
            first_record.get("qsnumber")
        )
        
        # Debug: Log what we got
        print(f"First record keys: {list(first_record.keys())}")
        print(f"Extracted QS Number: {first_qs}")
if not first_qs:
            os.remove(filepath)
            return jsonify({
                'error': 'QS Number column not found in Excel. Expected columns: QS Number, QS_Number, or QSNumber',
                'columns_found': list(first_record.keys())
            }), 400
        
        wo_context = extract_qsid_context(master_json, first_qs)
        
        if not wo_context:
            os.remove(filepath)
            return jsonify({'error': f'QS Number {first_qs} not found in master data'}), 404
        
        # Get work order ID
        wo_id = wo_context.get("Work Order No") or wo_context.get("WO_No")
        
        if not wo_id:
            os.remove(filepath)
            return jsonify({'error': 'Work Order ID not found in context'}), 400
        
        # Process through agent
        try:
            run_id = process_input_snapshot(snap, wo_id=str(wo_id), model_name=model_name)
        except ValueError as e:
            os.remove(filepath)
            return jsonify({'error': f'Work order processing failed: {str(e)}'}), 400
        
        # Clean up
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'run_id': run_id,
            'wo_id': str(wo_id),
            'qs_number': first_qs,
            'work_order_id': str(wo_id),
            'records_processed': len(records),
            'message': f'Processing completed successfully. {len(records)} records processed.'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/sample')
def api_sample():
    """Get sample file details."""
    return jsonify({
        'columns': [
            'QS Number',
            'Work Order No',
            'Change Type',
            'Target',
            'Old Value',
            'New Value',
            'Reason'
        ],
        'example': {
            'QS Number': 'QSAPA67',
            'Work Order No': 10479,
            'Change Type': 'Update',
            'Target': 'Substance List',
            'Old Value': 'Old substance',
            'New Value': 'New substance',
            'Reason': 'Regulatory update'
        }
    })


@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'File is too large. Maximum: 50MB'}), 413


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Work Order Agent - Excel Processor")
    print("="*60)
    print("\n📍 Opening: http://localhost:5000")
    print("📂 Context: data/work_orders_master.json")
    print("📊 Automatic QS Number detection")
    print("\n" + "="*60 + "\n")
    
    app.run(debug=True, port=5000)
