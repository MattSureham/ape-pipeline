# APE Pipeline - Automated Paper Evaluation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-green)](https://github.com/MattSureham/ape-pipeline)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> **Multi-field academic paper generation with AI-powered review and tournament ranking system**

APE Pipeline is a comprehensive academic paper generation system that supports multiple research fields, bilingual output (English/Chinese), and advanced features like tournament-based paper ranking and multi-format data loading.

---

## 🌟 Features

### 🎓 Multi-Field Support
Generate papers for **8 academic fields** with appropriate formatting:
- **Economics** (AER/QJE style) - DiD, RDD, IV, RCT
- **Psychology** (APA style) - Experiments, Surveys
- **Computer Science** (ACM style) - Algorithms, Benchmarks
- **Medicine** (NEJM style) - RCTs, Cohort studies
- **Sociology** (ASR style) - Ethnography, Interviews
- **Political Science** (APSR style) - Quantitative analysis
- **Education** (AERA style) - Quasi-experiments
- **Environmental Science** (Nature style) - Modeling

### 📁 Smart Data Loading
Import data and references from multiple formats:
- **Data**: CSV, JSON, Excel (.xlsx/.xls), DOCX, TXT, MD
- **References**: PDF, DOCX, TXT, MD, CAJ (Chinese Academic Journals)

### 🏆 Tournament System
- TrueSkill-based paper ranking
- Head-to-head paper comparison
- Leaderboard with conservative ratings

### 🔍 AI Review System
- Methodology review
- Fact checking
- Writing quality assessment

### 🌐 Bilingual Support
Generate papers in **English** or **Chinese** with proper academic formatting for each language.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- API key from [Moonshot](https://platform.moonshot.cn)

### Installation

```bash
# Clone repository
git clone https://github.com/MattSureham/ape-pipeline.git
cd ape-pipeline

# Install dependencies
pip install requests

# Configure API key
echo 'MOONSHOT_API_KEY="your-api-key-here"' > config/.env
```

### Basic Usage

```bash
# Generate an economics paper
./ape.sh generate "Minimum wage effects on employment" DiD

# Generate for specific field
./ape.sh generate-field "Social media and anxiety" psychology Survey

# Generate with data directories
./ape.sh generate-dir "HSR pollution study" economics DiD ./data ./refs

# Review a paper
./ape.sh review apep_20260225_xxxxxx

# Compare papers in tournament
./ape.sh tournament apep_xxx apep_yyy
./ape.sh leaderboard
```

### Windows PowerShell
```powershell
# Use PowerShell script
.\ape.ps1 generate "Topic" DiD
.\ape.ps1 generate-dir "Topic" field method .\data .\refs
```

---

## 📂 Project Structure

```
ape-pipeline/
├── ape.sh                    # Main bash script (macOS/Linux)
├── ape.ps1                   # PowerShell script (Windows)
├── config/
│   └── .env                  # API configuration (not committed)
├── scripts/
│   ├── generate_paper.py     # Paper generator
│   ├── review_paper.py       # Review system
│   ├── tournament.py         # Tournament & leaderboard
│   ├── smart_loader.py       # Multi-format file loader
│   └── md_to_pdf.py          # PDF conversion
├── papers/                   # Generated papers
├── examples/                 # Example projects
│   ├── data_dir/             # Sample data
│   ├── refs_dir/             # Sample references
│   └── chinese_project/      # Chinese source example
└── docs/                     # Documentation
    ├── DEPLOYMENT.md         # Complete setup guide
    ├── WINDOWS.md            # Windows-specific guide
    ├── CAJ-DOCX-GUIDE.md     # Chinese academic sources
    └── MULTI-FIELD-EXAMPLES.md # Field-specific examples
```

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [DEPLOYMENT.md](DEPLOYMENT.md) | Complete installation and usage guide |
| [WINDOWS.md](WINDOWS.md) | Windows installation (no WSL required) |
| [CAJ-DOCX-GUIDE.md](CAJ-DOCX-GUIDE.md) | Working with Chinese academic sources |
| [MULTI-FIELD-EXAMPLES.md](MULTI-FIELD-EXAMPLES.md) | Examples for all 8 fields |

---

## 🎯 Usage Examples

### Example 1: Basic Paper Generation
```bash
./ape.sh generate "Impact of minimum wage on employment" DiD
```

### Example 2: Multi-Field Paper
```bash
./ape.sh generate-field "Algorithm performance analysis" computer_science Benchmark
```

### Example 3: With Data Files
```bash
# Create project structure
mkdir -p myproject/data myproject/refs

# Add your files
cp survey_data.csv myproject/data/
cp references.pdf myproject/refs/

# Generate
./ape.sh generate-dir "Impact of X on Y" economics DiD myproject/data/ myproject/refs/
```

### Example 4: Bilingual Papers
```bash
# English paper
python scripts/generate_paper.py "HSR pollution effects" economics DiD data/ refs/ english

# Chinese paper
python scripts/generate_paper.py "高铁污染效应研究" economics DiD data/ refs/ chinese
```

### Example 5: Tournament Ranking
```bash
# Generate multiple papers
./ape.sh generate "Topic A" DiD  # ID: apep_xxx
./ape.sh generate "Topic B" DiD  # ID: apep_yyy

# Compare them
./ape.sh tournament apep_xxx apep_yyy
./ape.sh leaderboard
```

---

## 🛠️ Supported File Formats

### Data Directory
| Format | Support | Notes |
|--------|---------|-------|
| CSV | ✅ Full | Converted to markdown tables |
| JSON | ✅ Full | Formatted code blocks |
| Excel (.xlsx/.xls) | ✅ Full | Tables converted |
| DOCX | ✅ Full | Tables + text extracted |
| TXT / MD | ✅ Full | Plain text |

### References Directory
| Format | Support | Notes |
|--------|---------|-------|
| PDF | ✅ Full | Text extracted (first 5 pages) |
| DOCX | ✅ Full | Full text extracted |
| TXT / MD | ✅ Full | Plain text |
| CAJ | ⚠️ Partial | Metadata extracted, needs conversion |

---

## 🔄 Converting to PDF

### Method 1: Browser Print (Easiest)
```bash
# Generate HTML
python scripts/md_to_pdf.py papers/apep_xxxxxx.md

# Open in browser and print to PDF
open papers/apep_xxxxxx.html  # macOS
# or
start papers/apep_xxxxxx.html  # Windows
# Then: Cmd/Ctrl + P → Save as PDF
```

### Method 2: Pandoc
```bash
# Install pandoc and LaTeX
brew install pandoc
brew install --cask mactex  # macOS

# Convert
pandoc papers/apep_xxxxxx.md -o paper.pdf --pdf-engine=xelatex
```

### Method 3: VS Code Extension
Install "Markdown PDF" extension → Right-click → Export to PDF

---

## 🌏 Chinese Academic Sources

APE Pipeline supports Chinese Academic Journal (CAJ) files:

1. **Metadata extraction**: Filename, journal info captured
2. **Citation placeholders**: Automatic citation formatting
3. **Conversion support**: Works with CAJViewer exported PDFs

See [CAJ-DOCX-GUIDE.md](CAJ-DOCX-GUIDE.md) for details.

---

## 🐛 Troubleshooting

### "MOONSHOT_API_KEY not set"
```bash
echo 'MOONSHOT_API_KEY="your-key"' > config/.env
```

### "Permission denied: ape.sh"
```bash
chmod +x ape.sh
```

### Windows Execution Policy
```powershell
powershell -ExecutionPolicy Bypass -File .\ape.ps1
```

### Module not found
```bash
pip install requests
# Optional:
pip install pandas openpyxl PyPDF2 python-docx
```

---

## 📝 API Key Setup

1. Visit https://platform.moonshot.cn
2. Create an account
3. Generate API key
4. Add to `config/.env`:
```bash
MOONSHOT_API_KEY="sk-your-key-here"
```

---

## 🤝 Contributing

This project extends the original [APE (Automated Paper Evaluation)](https://github.com/SocialCatalystLab/ape-papers) with multi-field support and enhanced features.

---

## 📄 License

MIT License - See LICENSE file for details.

---

## 🙏 Acknowledgments

- Original APE concept by Social Catalyst Lab
- Moonshot AI for API support
- Contributors and testers

---

## 📬 Quick Reference

```bash
# Deploy
git clone https://github.com/MattSureham/ape-pipeline.git
cd ape-pipeline
pip install requests
echo 'MOONSHOT_API_KEY="key"' > config/.env

# Use
./ape.sh generate "Topic" DiD
./ape.sh generate-dir "Topic" field method data/ refs/
./ape.sh review apep_xxx
./ape.sh tournament apep_xxx apep_yyy
./ape.sh leaderboard
```

---

**Happy paper generating!** 🦆
