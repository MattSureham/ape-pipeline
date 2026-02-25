#!/usr/bin/env python3
"""
Convert Markdown to PDF using available tools
"""

import sys
import os
import subprocess
from pathlib import Path

def convert_md_to_pdf(md_file, pdf_file=None):
    """Convert markdown file to PDF"""
    md_path = Path(md_file)
    if not md_path.exists():
        print(f"Error: File not found: {md_file}")
        return False
    
    if pdf_file is None:
        pdf_file = md_path.with_suffix('.pdf')
    
    # Try pandoc first
    if subprocess.run(['which', 'pandoc'], capture_output=True).returncode == 0:
        print(f"Converting {md_file} to PDF using pandoc...")
        cmd = [
            'pandoc',
            str(md_file),
            '-o', str(pdf_file),
            '--pdf-engine=xelatex',
            '-V', 'CJKmainfont=SimHei',
            '-V', 'geometry:margin=1in',
            '--toc'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Created: {pdf_file}")
            return True
        else:
            print(f"Pandoc error: {result.stderr}")
    
    # Create HTML version as fallback
    print(f"Creating HTML version (open in browser to print to PDF)...")
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {{ font-family: "SimHei", "Heiti SC", "Microsoft YaHei", sans-serif; 
       max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
h1 {{ color: #333; border-bottom: 2px solid #333; padding-bottom: 10px; }}
h2 {{ color: #555; margin-top: 30px; }}
code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
pre {{ background: #f4f4f4; padding: 15px; overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background: #f0f0f0; }}
</style>
</head>
<body>
<pre>{md_content}</pre>
</body>
</html>"""
    
    html_file = md_path.with_suffix('.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created HTML: {html_file}")
    print(f"   Open in browser and print to PDF")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python md_to_pdf.py <markdown_file> [output_pdf]")
        sys.exit(1)
    
    md_file = sys.argv[1]
    pdf_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_md_to_pdf(md_file, pdf_file)
