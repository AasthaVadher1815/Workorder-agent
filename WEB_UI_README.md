# 🚀 Work Order Agent Web UI

A Flask-based web interface for processing work order Excel files with LLM context.

## Features

✅ **Upload Excel Files** - Drag & drop or click to upload  
✅ **Select Context** - Choose from 519+ loaded work orders  
✅ **LLM Processing** - Automatic processing with configurable model  
✅ **Database Integration** - Results stored and tracked  
✅ **Beautiful UI** - Modern, responsive interface  

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Web Server
```bash
python web_app.py
```

### 3. Open in Browser
```
http://localhost:5000
```

## How to Use

1. **Prepare Excel File**
   - Create Excel with columns: `QS Number`, `Work Order No`, `Change Type`, `Target`, `Old Value`, `New Value`, `Reason`
   - Or use our sample: `sample_input.xlsx`

2. **Upload File**
   - Drag and drop Excel file or click to browse
   - File validates automatically

3. **Select Work Order**
   - Choose from dropdown (shows WO ID, QS Number, description)
   - Shows 100 most recent work orders

4. **Configure Model** (optional)
   - Select LLM model: GPT-4, GPT-4 Mini, GPT-3.5 Turbo
   - Default: GPT-4 Mini

5. **Process**
   - Click "🚀 Process Excel"
   - Real-time status updates
   - Results displayed immediately

## Expected Excel Format

| QS Number | Work Order No | Change Type | Target | Old Value | New Value | Reason |
|-----------|---------------|------------|--------|-----------|-----------|--------|
| QSAPA67 | 10479 | Update | Substance List | Old substance | New substance | Regulatory update |
| QSAPA67 | 10479 | Add | CAS Number | | 120928-09-8 | New substance added |

## API Endpoints

### `GET /`
Main upload page

### `POST /upload`
Process Excel file
- **Form Data:**
  - `excel_file`: Excel file (required)
  - `context_id`: Selected work order (required) - format: `db:WO_ID`
  - `model_name`: LLM model name (optional, default: gpt-4-mini)

**Response:**
```json
{
  "success": true,
  "run_id": "uuid-string",
  "message": "Processing completed successfully"
}
```

### `GET /api/work-orders`
Get list of available work orders

**Response:**
```json
[
  {
    "wo_id": "10479",
    "qs_number": "QSAPA67",
    "short_name": "Japan. NITE GHS Classifications..."
  }
]
```

### `GET /api/contexts`
Get all available contexts (files + DB)

## File Structure

```
web/
├── templates/
│   └── index.html          # Main upload page
└── static/
    ├── style.css           # Styling
    └── script.js           # Client-side logic

uploads/                     # Temporary upload folder
web_app.py                   # Flask application
```

## Troubleshooting

### "No module named 'flask'"
```bash
pip install flask
```

### "Database connection failed"
Check `.env` file has `DATABASE_URL` set:
```
DATABASE_URL=mysql+pymysql://root:@localhost:3306/workorder_agent
```

### "Port 5000 already in use"
Change port in `web_app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Upload fails silently
1. Check file size (max 16MB)
2. Verify Excel format (xlsx/xls)
3. Check browser console for errors (F12)

## Production Deployment

For production, use proper WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
```

Or use Docker:
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "web_app:app"]
```

## Next Steps

- Implement Excel output generation
- Add progress tracking for large files
- Store results in database
- Create export functionality
- Add user authentication
- Deploy to cloud (AWS, GCP, Azure)

---

**Built with Flask + SQLAlchemy + pandas**
