# APE Pipeline - Complete Deployment & Usage Handbook

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Basic Usage](#basic-usage)
6. [Advanced Features](#advanced-features)
7. [Troubleshooting](#troubleshooting)

---

## Overview

APE Pipeline is a multi-field academic paper generation system that supports:
- 8 academic disciplines with field-specific formatting
- Multi-format data loading (CSV, JSON, Excel, DOCX, PDF, CAJ)
- Bilingual paper generation (English/Chinese)
- AI-powered review and tournament ranking
- Cross-platform support (macOS, Linux, Windows)

---

## Prerequisites

### System Requirements
- **OS**: macOS, Linux, or Windows (with Git Bash or PowerShell)
- **Python**: 3.8 or higher
- **Git**: For cloning the repository
- **Internet**: For API calls to AI providers
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB for installation, plus space for papers

### Required Software
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Check Git
git --version
```

### API Key Required
You need an API key from Moonshot (Kimi):
- Visit: https://platform.moonshot.cn
- Create account → API Keys → Generate

---

## Installation

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/MattSureham/ape-pipeline.git

# Navigate to the directory
cd ape-pipeline
```

### Step 2: Install Python Dependencies

```bash
# Required: Core dependency
pip3 install requests

# Optional: For Excel file support
pip3 install pandas openpyxl

# Optional: For PDF text extraction
pip3 install PyPDF2

# Optional: For DOCX support
pip3 install python-docx
```

### Step 3: Verify Installation

```bash
# Check if main script is executable (macOS/Linux)
ls -la ape.sh

# Test the help command
./ape.sh help
```

**Windows Users**: Use `ape.ps1` instead:
```powershell
.\ape.ps1 help
```

---

## Configuration

### Step 1: Create Config File

```bash
# Create the config directory if it doesn't exist
mkdir -p config

# Create the environment file
# macOS/Linux:
echo 'MOONSHOT_API_KEY="sk-your-actual-key-here"' > config/.env

# Windows PowerShell:
Set-Content -Path "config\.env" -Value 'MOONSHOT_API_KEY="sk-your-key"'
```

### Step 2: Verify Configuration

The `config/.env` file should look like:
```bash
MOONSHOT_API_KEY="sk-your-actual-key-from-moonshot"
```

**⚠️ IMPORTANT: Never commit this file to GitHub!**
The `.gitignore` file is already configured to exclude it.

### Step 3: Test Configuration

```bash
# Run a simple test
./ape.sh generate "Test paper" DiD

# Expected output:
# 📝 Generating paper: Test paper
#    Method: DiD
# ✅ Paper saved: papers/apep_20260225_123456.md
#    ID: apep_20260225_123456
```

If you see a paper ID, everything is working!

---

## Basic Usage

### Command Structure

```bash
./ape.sh [command] [arguments]
```

**Windows PowerShell:**
```powershell
.\ape.ps1 [command] [arguments]
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `generate` | Generate a basic paper | `./ape.sh generate "Topic" DiD` |
| `generate-field` | Generate for specific field | `./ape.sh generate-field "Topic" economics DiD` |
| `generate-dir` | Generate with data directories | `./ape.sh generate-dir "Topic" econ DiD data/ refs/` |
| `review` | Review a paper | `./ape.sh review apep_xxxxxx` |
| `tournament` | Compare two papers | `./ape.sh tournament apep_1 apep_2` |
| `leaderboard` | View rankings | `./ape.sh leaderboard` |
| `fields` | List supported fields | `./ape.sh fields` |
| `setup` | Edit configuration | `./ape.sh setup` |
| `help` | Show help | `./ape.sh help` |

### Example: Basic Paper Generation

```bash
# Generate an economics paper
./ape.sh generate "Minimum wage effects on employment" DiD

# Output:
# 📝 Generating paper: Minimum wage effects on employment
#    Method: DiD
# ✅ Paper saved: papers/apep_20260225_123456.md
#    ID: apep_20260225_123456
```

### Viewing the Paper

```bash
# View in terminal
cat papers/apep_20260225_123456.md

# Or open in text editor (macOS)
open papers/apep_20260225_123456.md

# Or use VS Code
code papers/apep_20260225_123456.md
```

---

## Advanced Features

### 1. Multi-Field Support

Generate papers for different academic fields:

```bash
# Economics (default)
./ape.sh generate-field "Minimum wage effects" economics DiD

# Psychology
./ape.sh generate-field "Social media and anxiety" psychology "Survey"

# Computer Science
./ape.sh generate-field "New graph neural network" computer_science "Benchmark"

# Medicine
./ape.sh generate-field "Drug X effectiveness" medicine "RCT"

# Sociology
./ape.sh generate-field "Gentrification effects" sociology "Ethnography"

# Political Science
./ape.sh generate-field "Voting behavior" political_science "Quantitative"

# Education
./ape.sh generate-field "Online learning outcomes" education "Quasi-experiment"

# Environmental Science
./ape.sh generate-field "Climate change impacts" environmental_science "Modeling"
```

### 2. Using Data Directories

Organize your project with separate data and references folders:

```bash
# Create project structure
mkdir -p myproject/data myproject/refs

# Add data files (CSV, JSON, Excel, TXT, MD, DOCX)
cp my_data.csv myproject/data/
cp policy_info.json myproject/data/
cp experiment_notes.docx myproject/data/

# Add reference files (PDF, TXT, MD, DOCX)
cp references.pdf myproject/refs/
cp bibliography.txt myproject/refs/
cp paper.docx myproject/refs/

# Generate paper with all files
./ape.sh generate-dir \
  "Impact of policy X on outcome Y" \
  economics \
  "Difference-in-Differences" \
  myproject/data/ \
  myproject/refs/
```

### 3. Supported File Formats

#### Data Directory:
- **CSV** → Converted to markdown tables
- **JSON** → Formatted as code blocks
- **Excel (.xlsx/.xls)** → Converted to tables
- **DOCX** → Tables and text extracted
- **TXT/MD** → Plain text

#### References Directory:
- **PDF** → Text extracted (first 5 pages)
- **DOCX** → Full text extracted
- **TXT/MD** → Plain text
- **CAJ** → Metadata extracted (Chinese Academic Journals)

### 4. Tournament System

Compare multiple papers:

```bash
# Generate two papers
./ape.sh generate "Topic A" DiD
# Note the ID: apep_20260225_111111

./ape.sh generate "Topic B" DiD
# Note the ID: apep_20260225_222222

# Run tournament
./ape.sh tournament apep_20260225_111111 apep_20260225_222222

# View leaderboard
./ape.sh leaderboard
```

### 5. Review System

Get detailed feedback on papers:

```bash
# Review a paper
./ape.sh review apep_20260225_xxxxxx

# This generates:
# - Methodology review
# - Fact checking
# - Writing quality assessment
# - Saved to papers/reviews/
```

### 6. Bilingual Papers (Chinese/English)

Generate papers in both languages:

```bash
# English paper
python3 scripts/generate_paper.py \
  "Impact of HSR on urban air pollution" \
  economics \
  "DiD" \
  data/ \
  refs/ \
  english

# Chinese paper
python3 scripts/generate_paper.py \
  "高铁开通对城市空气污染的影响研究" \
  economics \
  "双重差分法" \
  data/ \
  refs/ \
  chinese
```

---

## Workflow Examples

### Complete Research Workflow

```bash
# 1. Create project
mkdir -p projects/my_research/{data,refs}

# 2. Add your data
cp ~/Downloads/survey_data.csv projects/my_research/data/
cp ~/Downloads/literature_review.pdf projects/my_research/refs/

# 3. Generate paper
./ape.sh generate-dir \
  "Impact of X on Y in Z context" \
  economics \
  "Difference-in-Differences" \
  projects/my_research/data/ \
  projects/my_research/refs/

# 4. Review the paper
./ape.sh review apep_20260225_xxxxxx

# 5. Generate alternative version
./ape.sh generate-dir \
  "Impact of X on Y - Alternative specification" \
  economics \
  "RDD" \
  projects/my_research/data/ \
  projects/my_research/refs/

# 6. Compare papers
./ape.sh tournament apep_20260225_xxxxxx apep_20260225_yyyyyy

# 7. Check rankings
./ape.sh leaderboard
```

---

## Converting to PDF

### Method 1: Browser Print (Easiest)

```bash
# Generate HTML first
python3 scripts/md_to_pdf.py papers/apep_xxxxxx.md

# Open in browser
open papers/apep_xxxxxx.html  # macOS
start papers/apep_xxxxxx.html  # Windows

# Then press Ctrl+P (or Cmd+P) → Save as PDF
```

### Method 2: Pandoc (Best Quality)

```bash
# Install pandoc and LaTeX
brew install pandoc
brew install --cask mactex  # macOS

# Convert to PDF
pandoc papers/apep_xxxxxx.md -o paper.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in
```

### Method 3: VS Code Extension

1. Install VS Code: https://code.visualstudio.com/
2. Install "Markdown PDF" extension
3. Right-click .md file → Markdown PDF: Export (pdf)

---

## Troubleshooting

### Issue: "MOONSHOT_API_KEY not set"

**Solution:**
```bash
# Edit config file
nano config/.env

# Add your key
MOONSHOT_API_KEY="sk-your-key-here"
```

### Issue: "Module not found: requests"

**Solution:**
```bash
pip3 install requests
```

### Issue: "Permission denied: ape.sh"

**Solution:**
```bash
chmod +x ape.sh
```

### Issue: Chinese characters not displaying

**Solution:**
- The HTML output uses UTF-8 encoding
- Open in a browser that supports Chinese fonts
- For PDF conversion, use a tool that supports CJK fonts

### Issue: CAJ files not loading

**Solution:**
CAJ files require manual conversion:
1. Open in CAJViewer (Windows software)
2. Export to PDF
3. Place PDF in refs/ directory

Or create a metadata text file with citation info.

### Issue: API rate limits

**Solution:**
- The pipeline will show errors if API limits are reached
- Wait a few minutes and try again
- Consider upgrading your Moonshot plan

### Windows-Specific Issues

**Execution Policy:**
```powershell
# Run as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or bypass for this session:
powershell -ExecutionPolicy Bypass -File .\ape.ps1
```

**Python not found:**
```powershell
# Try python3
python3 scripts\generate_paper.py "test" economics DiD

# Or use full path
C:\Python39\python.exe scripts\generate_paper.py "test" economics DiD
```

---

## Project Structure Reference

```
ape-pipeline/
├── README.md                 # Main documentation
├── DEPLOYMENT.md             # This file
├── WINDOWS.md                # Windows-specific guide
├── CAJ-DOCX-GUIDE.md         # Chinese source handling
├── MULTI-FIELD-EXAMPLES.md   # Field examples
├── ape.sh                    # Main bash script (macOS/Linux)
├── ape.ps1                   # PowerShell script (Windows)
├── config/
│   └── .env                  # API keys (not committed)
├── scripts/
│   ├── generate_paper.py     # Paper generator
│   ├── review_paper.py       # Review system
│   ├── tournament.py         # Tournament system
│   ├── smart_loader.py       # Multi-format loader
│   └── md_to_pdf.py          # PDF conversion
├── papers/                   # Generated papers
│   ├── apep_*.md             # Paper files
│   └── reviews/              # Review files
├── examples/                 # Example projects
│   ├── data_dir/             # Sample data
│   ├── refs_dir/             # Sample references
│   └── chinese_project/      # Chinese source example
├── projects/                 # Your projects (created by you)
└── tournaments/              # Tournament data
```

---

## Tips for Best Results

1. **Be Specific**: Use detailed research questions
   - ❌ "Minimum wage effects"
   - ✅ "Minimum wage effects on teen fast food employment in NJ 1991-1993"

2. **Add Real Data**: The AI works better with actual data files

3. **Organize by Project**: Keep each study in its own directory

4. **Review Before Tournament**: Review papers individually before comparing

5. **Iterate**: Generate multiple versions and compare

6. **Save API Key Securely**: Never commit config/.env to Git

---

## Quick Reference Card

```bash
# Deploy
git clone https://github.com/MattSureham/ape-pipeline.git
cd ape-pipeline
pip3 install requests
echo 'MOONSHOT_API_KEY="your-key"' > config/.env

# Basic use
./ape.sh generate "Topic" DiD
./ape.sh generate-dir "Topic" economics DiD data/ refs/
./ape.sh review apep_xxx
./ape.sh tournament apep_xxx apep_yyy
./ape.sh leaderboard

# Windows PowerShell
.\ape.ps1 generate "Topic" DiD
```

---

**Happy paper generating!** 🦆
