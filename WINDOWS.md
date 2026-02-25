# APE Pipeline - Windows Installation Guide

## Quick Start for Windows (PowerShell)

### Step 1: Prerequisites

```powershell
# Check Python (should be 3.8+)
python --version
# or
python3 --version

# Check Git
git --version
```

### Step 2: Clone Repository

```powershell
# Clone
git clone https://github.com/MattSureham/ape-pipeline.git
cd ape-pipeline
```

### Step 3: Install Dependencies

```powershell
# Install Python packages
pip install requests

# Optional: For Excel files
pip install pandas openpyxl

# Optional: For PDF support
pip install PyPDF2

# Optional: For DOCX support
pip install python-docx
```

### Step 4: Configure API Key

```powershell
# Create config directory
mkdir config

# Create config file with your API key
Set-Content -Path "config\.env" -Value 'MOONSHOT_API_KEY="your-api-key-here"'
```

Get your API key from: https://platform.moonshot.cn

### Step 5: Test Installation

```powershell
# Test Python directly
python scripts\generate_paper.py "Test paper" economics DiD
```

Or use the PowerShell script:
```powershell
# Using PowerShell script
.\ape.ps1 generate "Test paper" DiD
```

---

## PowerShell Commands Reference

| Task | Command |
|------|---------|
| **Generate paper** | `.\ape.ps1 generate "Topic" DiD` |
| **Multi-field** | `.\ape.ps1 generate-field "Topic" economics DiD` |
| **With directories** | `.\ape.ps1 generate-dir "Topic" econ DiD .\data .\refs` |
| **Review** | `.\ape.ps1 review apep_xxxxxx` |
| **Tournament** | `.\ape.ps1 tournament apep_xxx apep_yyy` |
| **Leaderboard** | `.\ape.ps1 leaderboard` |
| **List fields** | `.\ape.ps1 fields` |
| **Edit config** | `.\ape.ps1 setup` |

---

## Directory Structure for Windows

```
D:\ape-pipeline\
├── ape.ps1                   # PowerShell script
├── ape.sh                    # Bash script (for Git Bash)
├── config\
│   └── .env                  # API key
├── scripts\
│   ├── generate_paper.py     # Paper generator
│   ├── review_paper.py       # Review system
│   ├── tournament.py         # Tournament
│   └── ...
├── papers\                   # Generated papers
│   └── apep_*.md
├── data\                     # Your data (you create this)
└── refs\                     # Your references (you create this)
```

---

## Example Workflow

### 1. Create Project

```powershell
# Create directories for your project
mkdir myproject
cd myproject
mkdir data
mkdir refs
```

### 2. Add Your Files

```powershell
# Copy data files
copy C:\Users\YourName\Documents\data.csv data\
copy C:\Users\YourName\Documents\references.pdf refs\
```

### 3. Generate Paper

```powershell
cd D:\ape-pipeline

.\ape.ps1 generate-dir "Impact of X on Y" economics DiD .\myproject\data .\myproject\refs
```

### 4. View Results

```powershell
# List generated papers
Get-ChildItem papers\*.md

# View a paper
notepad papers\apep_xxxxxxxx.md

# Or use VS Code
code papers\apep_xxxxxxxx.md
```

---

## Converting to PDF on Windows

### Method 1: Browser Print (Recommended)

```powershell
# Generate HTML first
python scripts\md_to_pdf.py papers\apep_xxxxxx.md

# Open in browser
start papers\apep_xxxxxx.html

# Then press Ctrl+P → Save as PDF
```

### Method 2: Install Pandoc

```powershell
# Install pandoc
choco install pandoc
# or download from https://pandoc.org/installing.html

# Convert to PDF
pandoc papers\apep_xxxxxx.md -o paper.pdf
```

### Method 3: VS Code Extension

1. Install VS Code: https://code.visualstudio.com/
2. Install "Markdown PDF" extension
3. Right-click .md file → Markdown PDF: Export (pdf)

---

## Common Windows Issues

### Issue: "python" not found

**Solution:**
```powershell
# Try python3
python3 scripts\generate_paper.py "test" economics DiD

# Or use full path
C:\Python39\python.exe scripts\generate_paper.py "test" economics DiD
```

### Issue: Execution Policy

**Solution:**
```powershell
# Run as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or bypass for this session only:
powershell -ExecutionPolicy Bypass -File .\ape.ps1 generate "test" DiD
```

### Issue: Permission Denied

**Solution:**
```powershell
# Unblock the script
Unblock-File -Path .\ape.ps1

# Or run with bypass
powershell -ExecutionPolicy Bypass -File .\ape.ps1
```

### Issue: CAJ Files Not Working

**Solution:**
CAJ files are Chinese Academic Journal format. On Windows:
1. Install CAJViewer from CNKI
2. Open CAJ file → Export as PDF
3. Place PDF in `refs\` folder

---

## File Paths in Windows

**Important:** Use backslashes (`\`) or forward slashes (`/`) in PowerShell:

```powershell
# Both work:
.\ape.ps1 generate "test" DiD
./ape.ps1 generate "test" DiD

# For directories:
.\ape.ps1 generate-dir "test" econ DiD .\data .\refs
.\ape.ps1 generate-dir "test" econ DiD data/ refs/
```

---

## Alternative: Using Python Directly

If PowerShell scripts don't work, use Python directly:

```powershell
# Generate paper
python scripts\generate_paper.py "Topic" economics DiD

# Generate with data
python scripts\generate_paper.py "Topic" economics DiD data/ refs/

# Review
python scripts\review_paper.py apep_xxxxxx

# Tournament
python scripts\tournament.py match apep_xxx apep_yyy
python scripts\tournament.py leaderboard
```

---

## Quick Reference Card (Windows)

```powershell
# Deploy
git clone https://github.com/MattSureham/ape-pipeline.git
cd ape-pipeline
pip install requests
Set-Content -Path "config\.env" -Value 'MOONSHOT_API_KEY="your-key"'

# Basic use
.\ape.ps1 generate "Topic" DiD

# With data
.\ape.ps1 generate-dir "Topic" econ DiD .\data .\refs

# Review & compare
.\ape.ps1 review apep_xxx
.\ape.ps1 tournament apep_xxx apep_yyy
.\ape.ps1 leaderboard

# Convert to PDF
python scripts\md_to_pdf.py papers\apep_xxx.md
start papers\apep_xxx.html  # Then Ctrl+P → Save as PDF
```

---

## Need Help?

- Check `DEPLOYMENT.md` for general usage
- Check `CAJ-DOCX-GUIDE.md` for Chinese source handling
- Check `MULTI-FIELD-EXAMPLES.md` for field examples

---

**Happy paper generating on Windows!** 🦆
