# Quick Start Guide - Professional UI

## 🚀 Getting Started

### 1. Start the Application
```bash
cd c:\Users\AsthaVadher\Downloads\workorder-agent
python web_app.py
```

### 2. Open in Browser
```
http://localhost:5000
```

You'll see a professional 3-step interface with:
- Professional header with "Ready" status indicator
- Step 1: Upload Excel file
- Step 2: Configure LLM model
- Step 3: Process button

## 📋 How to Use

### Step 1: Upload Excel File
1. **Drag & Drop:** Drag your Excel file onto the upload zone
2. **Or Click:** Click the upload zone to browse for a file
3. **Validation:** System checks file type (.xlsx, .xls) and size (max 50MB)
4. **Success:** You'll see a checkmark with file name and size
5. **Button Enabled:** The "Process Excel" button becomes enabled

### Step 2: Choose LLM Model
Select which model to use:
- **GPT-4 Mini (Fast)** - Fastest, good for simple changes
- **GPT-4 (Accurate)** - Most accurate, better reasoning
- **GPT-3.5 Turbo (Budget)** - Most economical option

The context source field shows: `work_orders_master.json` (automatically loaded)

### Step 3: Process
1. Click the **"🚀 Process Excel"** button
2. System automatically:
   - Extracts QS Number from your Excel file (first row)
   - Loads work_orders_master.json
   - Finds matching work order context
   - Processes through LLM with appropriate context
3. Watch the loading status appear
4. See results once processing completes

## 📊 Expected Results

After processing, you'll see:
- ✅ **Run ID** - Unique identifier for this processing run
- ✅ **QS Number** - Detected from your Excel file
- ✅ **Work Order ID** - Found from master data based on QS Number
- ✅ **Status** - Processing result (success/error)
- ✅ **Records Processed** - Number of change records processed
- ✅ **Download Button** - If applicable, download output file

## 📝 Excel File Format

Your Excel file should have columns:
```
QS Number | Work Order No | Change Type | Target | Old Value | New Value | Reason
```

**Important:** The QS Number from the FIRST ROW is automatically detected and used to find the matching work order context in `work_orders_master.json`.

Example first row:
```
QSAPA67 | 10479 | Update | Substance List | Old substance | New substance | Regulatory update
```

## 🔍 Key Features

### ✨ Automatic Detection
- QS Number: Auto-detected from Excel (no manual entry needed)
- Context: Auto-loaded from work_orders_master.json
- Work Order: Auto-matched based on QS Number
- No manual selections required!

### 🎨 Professional Design
- Modern gradient background (purple/blue theme)
- Responsive layout (works on desktop, tablet, mobile)
- Professional typography and spacing
- Smooth animations and transitions
- Clear visual hierarchy with numbered steps

### 🛡️ Error Handling
- Invalid file type → Shows error message
- File too large → Shows size limit
- QS Number not found → Shows helpful error
- Processing errors → Displays error details

### 📱 Responsive Design
- **Desktop:** Full 3-step card layout
- **Tablet:** Adjusted spacing and font sizes
- **Mobile:** Optimized for small screens

## ⚙️ Technical Details

### Backend Workflow
```
User uploads Excel
    ↓
Flask receives file
    ↓
Parse Excel → Extract QS Number from first row
    ↓
Load work_orders_master.json
    ↓
Search for matching QS Number in master data
    ↓
Extract work order context
    ↓
Process through LLM agent with context
    ↓
Return run_id + results
    ↓
Browser displays results
```

### Files Involved
- **web_app.py** - Flask application
- **web/templates/index.html** - UI structure
- **web/static/style.css** - Professional styling
- **web/static/script.js** - Client-side logic
- **data/work_orders_master.json** - Master context data

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
python web_app.py  # Change port in code or use different port
```

### Master JSON Encoding Error
If you see: `'charmap' codec can't decode byte`
- The JSON file uses UTF-8 encoding
- This is handled automatically by the system
- If you manually edit it, ensure UTF-8 encoding

### QS Number Not Found
If you get: `QS Number X not found in master data`
- Verify the QS Number in your Excel file
- Check work_orders_master.json has this QS Number
- Ensure Excel is using correct column format

### File Upload Issues
- Use Chrome, Edge, or Firefox (latest versions)
- Ensure file is .xlsx or .xls format
- File must be under 50MB
- Excel file must have columns: QS Number, Work Order No, etc.

## 🎯 What's Automatic (No Manual Steps Needed)

- ✅ QS Number detection from Excel
- ✅ Master JSON loading
- ✅ Work order context matching
- ✅ LLM processing
- ✅ Result formatting

## ❌ What Was Removed (As Requested)

- ❌ Work order selection dropdown
- ❌ Manual context selection
- ❌ Complex form fields
- ❌ User selection burden

## 📞 Support Info

**Application:** Work Order Processor v1.0
**Status:** Professional, Launch-Ready
**Technology:** Flask + Modern Web UI
**Context Source:** work_orders_master.json (519 records)
**Database:** MySQL with 7 tables

## 🚀 Ready to Deploy

Your application is:
- ✅ Professional and modern
- ✅ Fully automatic (no manual selections)
- ✅ Launch-ready
- ✅ Responsive (mobile-friendly)
- ✅ Well-tested
- ✅ Error-handled
- ✅ User-friendly

**Open http://localhost:5000 to see the professional UI in action!**
