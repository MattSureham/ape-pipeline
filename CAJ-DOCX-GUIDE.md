# APE Pipeline - CAJ and DOCX Support

## 📄 New Formats Supported

### For Data Directory:
- ✅ CSV, JSON, Excel (.xlsx/.xls)
- ✅ **DOCX** (Word documents with tables/text)
- ✅ TXT, MD
- ⚠️ **CAJ** (metadata only - see below)

### For References Directory:
- ✅ PDF, TXT, MD
- ✅ **DOCX** (Word documents)
- ⚠️ **CAJ** (Chinese Academic Journals - metadata + conversion info)

---

## 📝 Using DOCX Files

### As Data Source
Put `.docx` files in your `data/` directory:

```
myproject/
├── data/
│   ├── survey_results.docx    ← Word file with tables
│   └── notes.docx             ← Text notes
└── refs/
    └── references.docx        ← Citation list
```

**The pipeline will:**
- Extract tables from DOCX and convert to markdown
- Extract text content
- Include both in the paper

### As References
Put `.docx` files in your `refs/` directory:

```bash
./ape.sh generate-dir "Question" economics DiD data/ refs/
```

**The pipeline will:**
- Extract all text from the DOCX
- Include as references in literature review

---

## 🇨🇳 Using CAJ Files (Chinese Academic Journals)

CAJ files are proprietary format from CNKI (China National Knowledge Infrastructure).

### Current Support

The pipeline handles CAJ files in **two ways**:

#### Option 1: Metadata-Only (Automatic)
If you put `.caj` files directly in `refs/`:

```
refs/
├── paper1.caj
└── paper2.caj
```

The pipeline will:
- Record filename and size
- Add citation placeholder
- Include instructions for conversion

#### Option 2: Convert to PDF (Recommended)

**Step 1:** Convert CAJ to PDF using CAJViewer or caj2pdf:

```bash
# Install converter
pip install caj2pdf

# Convert files
caj2pdf -i paper.caj -o paper.pdf
```

**Step 2:** Put converted PDFs in `refs/`:

```
refs/
├── paper1.pdf    ← Converted from .caj
└── paper2.pdf
```

The pipeline will extract full text from PDFs.

#### Option 3: Create Metadata Files

Create `.txt` files with citation info:

```
refs/
├── wang_2023.caj              ← Original file
└── wang_2023.txt              ← Metadata you create
```

**wang_2023.txt** content:
```
Title: 高校毕业生就业影响因素研究
Journal: 中国高教研究
Authors: 王伟, 李明
Year: 2023
Volume: 45(3)
Pages: 45-58
Abstract: [paste abstract here]
```

---

## 🚀 Complete Example

### Project Structure

```
chinese_employment_study/
├── data/
│   ├── survey_data.csv          # Statistical data
│   ├── university_list.docx     # List of universities
│   └── methodology_notes.txt    # Research notes
└── refs/
    ├── wang_2023.caj            # CAJ file (metadata extracted)
    ├── li_2022.pdf              # Converted PDF
    └── bibliography.txt         # Additional citations
```

### Generate Paper

```bash
cd /Users/matthew/.openclaw/workspace/ape-pipeline

./ape.sh generate-dir \
  "Graduate employment in Chinese universities" \
  economics \
  "Regression analysis" \
  chinese_employment_study/data/ \
  chinese_employment_study/refs/
```

### What Happens

1. **CSV** → Converted to markdown table in paper
2. **DOCX** → Tables extracted and included
3. **TXT** → Included as notes/methodology
4. **CAJ** → Metadata recorded, citation added
5. **PDF** → Full text extracted and cited

---

## 📋 Supported Format Summary

| Format | Data Dir | Refs Dir | Notes |
|--------|----------|----------|-------|
| CSV | ✅ Full | ✅ Full | Tables converted |
| JSON | ✅ Full | ✅ Full | Formatted |
| Excel | ✅ Full | ✅ Full | Tables converted |
| DOCX | ✅ Full | ✅ Full | Tables + text |
| PDF | ❌ No | ✅ Full | Text extracted |
| CAJ | ⚠️ Meta | ⚠️ Meta | Needs conversion |
| TXT | ✅ Full | ✅ Full | Plain text |
| MD | ✅ Full | ✅ Full | Markdown |

---

## 🔧 Installing Dependencies

For full DOCX support:
```bash
pip install python-docx
```

For CAJ to PDF conversion:
```bash
pip install caj2pdf
```

For PDF text extraction:
```bash
pip install PyPDF2
```

---

## 💡 Tips for Chinese Academic Sources

1. **CAJ Files**: Always note the original Chinese title and journal name
2. **DOCX Files**: Use tables for structured data
3. **Citation Format**: The AI will format citations appropriately
4. **Mixed Sources**: You can mix English and Chinese sources

---

## Example Output

When using CAJ files, the paper will include:

```markdown
## References

Wang, W., & Li, M. (2023). 高校毕业生就业影响因素研究 
[Study on factors affecting graduate employment]. 
中国高教研究 [China Higher Education Research], 45(3), 45-58.
(CAJ format - full text in repository)
```

**Ready to use Chinese academic sources!** 🇨🇳
