// Global variables
let uploadedFile = null;

document.addEventListener('DOMContentLoaded', function() {
    // Setup upload zone
    const uploadZone = document.getElementById('uploadZone');
    const excelFile = document.getElementById('excelFile');
    const processBtn = document.getElementById('processBtn');
    
    // Click to browse
    uploadZone.addEventListener('click', () => excelFile.click());
    
    // Drag and drop
    uploadZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadZone.classList.add('dragover');
    });
    
    uploadZone.addEventListener('dragleave', () => {
        uploadZone.classList.remove('dragover');
    });
    
    uploadZone.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadZone.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    });
    
    // File input change
    excelFile.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileSelect(e.target.files[0]);
        }
    });
    
    // Process button
    processBtn.addEventListener('click', handleProcessing);
});

function handleFileSelect(file) {
    const uploadZone = document.getElementById('uploadZone');
    const fileStatus = document.getElementById('fileStatus');
    const processBtn = document.getElementById('processBtn');
    
    // Validate file
    const validTypes = ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'];
    const isValidType = validTypes.includes(file.type) || file.name.match(/\.(xlsx?|xls)$/i);
    const isValidSize = file.size <= 50 * 1024 * 1024; // 50MB
    
    if (!isValidType) {
        showError(fileStatus, 'Invalid file type. Please upload an Excel file (.xlsx or .xls)');
        return;
    }
    
    if (!isValidSize) {
        showError(fileStatus, 'File is too large. Maximum size is 50MB');
        return;
    }
    
    // Store file
    uploadedFile = file;
    
    // Show success
    showSuccess(fileStatus, `${file.name} (${formatFileSize(file.size)})`);
    
    // Enable process button
    processBtn.disabled = false;
}

function showError(element, message) {
    element.textContent = `❌ ${message}`;
    element.className = 'file-status error';
}

function showSuccess(element, message) {
    element.textContent = `✓ ${message}`;
    element.className = 'file-status success';
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

async function handleProcessing() {
    if (!uploadedFile) {
        alert('Please select an Excel file first');
        return;
    }
    
    const processBtn = document.getElementById('processBtn');
    const modelSelect = document.getElementById('modelSelect');
    const resultArea = document.getElementById('resultArea');
    const statusBox = document.getElementById('statusBox');
    const resultBox = document.getElementById('resultBox');
    
    // Disable button and show loading
    processBtn.disabled = true;
    processBtn.innerHTML = '<span class="loading-spinner"></span> Processing...';
    
    // Show result area with loading status
    resultArea.style.display = 'block';
    statusBox.className = 'status-box loading';
    statusBox.innerHTML = `
        <span class="status-icon">⏳</span>
        <div class="status-text">
            <strong>Processing your Excel file...</strong>
            <p>Detecting QS Number and loading context. This may take a moment.</p>
        </div>
    `;
    resultBox.style.display = 'none';
    
    try {
        // Prepare form data
        const formData = new FormData();
        formData.append('excel_file', uploadedFile);
        formData.append('model_name', modelSelect.value);
        
        // Send to server
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Success
            statusBox.className = 'status-box success';
            statusBox.innerHTML = `
                <span class="status-icon">✅</span>
                <div class="status-text">
                    <strong>Processing Complete!</strong>
                    <p>Your work order has been processed successfully.</p>
                </div>
            `;
            
            // Show results
            resultBox.style.display = 'block';
            displayResults(data, resultBox);
        } else {
            // Error response
            statusBox.className = 'status-box error';
            const errorMsg = data.error || 'An unknown error occurred';
            statusBox.innerHTML = `
                <span class="status-icon">❌</span>
                <div class="status-text">
                    <strong>Processing Failed</strong>
                    <p>${errorMsg}</p>
                </div>
            `;
        }
    } catch (error) {
        // Network error
        statusBox.className = 'status-box error';
        statusBox.innerHTML = `
            <span class="status-icon">❌</span>
            <div class="status-text">
                <strong>Error</strong>
                <p>${error.message}</p>
            </div>
        `;
    } finally {
        // Re-enable button
        processBtn.disabled = false;
        processBtn.innerHTML = '<span class="btn-icon">🚀</span><span class="btn-text">Process Excel</span>';
    }
}

function displayResults(data, resultBox) {
    let html = '<div class="result-box">';
    
    // Display run ID
    if (data.run_id) {
        html += `
            <div class="result-item">
                <strong>Run ID:</strong>
                <div class="result-item-value">${data.run_id}</div>
            </div>
        `;
    }
    
    // Display QS Number
    if (data.qs_number) {
        html += `
            <div class="result-item">
                <strong>QS Number:</strong>
                <div class="result-item-value">${data.qs_number}</div>
            </div>
        `;
    }
    
    // Display Work Order
    if (data.work_order_id) {
        html += `
            <div class="result-item">
                <strong>Work Order ID:</strong>
                <div class="result-item-value">${data.work_order_id}</div>
            </div>
        `;
    }
    
    // Display Status
    if (data.status) {
        html += `
            <div class="result-item">
                <strong>Status:</strong>
                <div class="result-item-value">${data.status}</div>
            </div>
        `;
    }
    
    // Display Output File
    if (data.output_file) {
        html += `
            <div class="result-item">
                <strong>Output File:</strong>
                <a href="${data.output_file}" class="download-btn" download>Download Results</a>
            </div>
        `;
    }
    
    // Display Records Processed
    if (data.records_processed) {
        html += `
            <div class="result-item">
                <strong>Records Processed:</strong>
                <div class="result-item-value">${data.records_processed}</div>
            </div>
        `;
    }
    
    html += '</div>';
    resultBox.innerHTML = html;
}

