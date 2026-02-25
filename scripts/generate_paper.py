#!/usr/bin/env python3
"""
APE Paper Generator with Chinese Language Support
Generates academic papers in English or Chinese
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from smart_loader import load_directory

def load_env():
    env_path = Path(__file__).parent.parent / "config" / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

load_env()

class MoonshotProvider:
    """Moonshot AI Provider"""
    def __init__(self, api_key=None, model="moonshot-v1-8k"):
        self.api_key = api_key or os.getenv("MOONSHOT_API_KEY")
        self.model = model
        self.base_url = "https://api.moonshot.cn/v1"
    
    def generate(self, prompt, system="", max_tokens=8192):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json={
                "model": self.model,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": 0.7
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

def load_file_or_directory(path, is_data=True):
    """Load content from file or directory"""
    if not path:
        return ""
    
    p = Path(path)
    
    if p.is_dir():
        if is_data:
            data, _ = load_directory(data_dir=str(p))
            return data
        else:
            _, refs = load_directory(refs_dir=str(p))
            return refs
    elif p.is_file():
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print(f"⚠️  Path not found: {path}")
        return ""

def get_field_config(field, language="english"):
    """Get configuration for different fields and languages"""
    
    if language == "chinese":
        configs = {
            "economics": {
                "journal": "《经济研究》/《管理世界》",
                "structure": ["标题", "摘要", "引言", "文献综述", "研究设计", "数据与实证", "结果分析", "结论与政策建议"],
                "format": "中文学术论文格式",
                "style": "严谨的因果识别分析，符合国内顶级经济学期刊规范"
            }
        }
    else:
        configs = {
            "economics": {
                "journal": "AER/QJE",
                "structure": ["Title", "Abstract", "Introduction", "Literature Review", "Empirical Strategy", "Data", "Results", "Conclusion"],
                "format": "LaTeX",
                "style": "Rigorous empirical analysis with causal identification"
            }
        }
    
    return configs.get(field.lower(), configs["economics"])

def generate_paper(question, field="economics", method="", data_path=None, refs_path=None, language="english"):
    """Generate academic paper in specified language"""
    
    config = get_field_config(field, language)
    
    print(f"📂 Loading data/references...")
    data_content = load_file_or_directory(data_path, is_data=True) if data_path else ""
    refs_content = load_file_or_directory(refs_path, is_data=False) if refs_path else ""
    
    api_key = os.getenv("MOONSHOT_API_KEY")
    if not api_key:
        print("❌ MOONSHOT_API_KEY not set")
        sys.exit(1)
    
    ai = MoonshotProvider(api_key=api_key)
    
    if language == "chinese":
        system_prompt = f"""你是一位顶尖经济学家，为{config['journal']}撰写论文。

论文结构：{', '.join(config['structure'])}
格式：{config['format']}
风格：{config['style']}

重要：使用提供的中文数据。不要编造数字。
如果提供了中文文献，请在文献综述中引用。"""

        prompt = f"""研究题目：{question}

研究方法：{method if method else '双重差分法 (DiD)'}
"""
        
        if data_content:
            prompt += f"""

研究数据：
```
{data_content[:8000]}
```"""
        
        if refs_content:
            prompt += f"""

参考文献：
```
{refs_content[:5000]}
```"""
        
        prompt += f"""

请生成完整的中文经济学论文，包括：
{chr(10).join([f"{i+1}. {section}" for i, section in enumerate(config['structure'])])}

使用规范的学术中文写作。包含DiD模型的数学公式。
在文献综述中引用提供的中文参考文献。"""

    else:  # English
        system_prompt = f"""You are an expert economist writing for {config['journal']}.

Paper Structure: {', '.join(config['structure'])}
Format: {config['format']}
Style: {config['style']}

Use the provided REAL DATA. Do not fabricate numbers."""

        prompt = f"""Research Question: {question}

Methodology: {method if method else 'Difference-in-Differences (DiD)'}
"""
        
        if data_content:
            prompt += f"""

REAL DATA:
```
{data_content[:8000]}
```"""
        
        if refs_content:
            prompt += f"""

REFERENCES:
```
{refs_content[:5000]}
```"""
        
        prompt += f"""

Generate a complete economics research paper with:
{chr(10).join([f"{i+1}. {section}" for i, section in enumerate(config['structure'])])}

Use LaTeX formatting. Include DiD methodology formulas."""
    
    lang_display = "Chinese" if language == "chinese" else "English"
    print(f"📝 Generating {lang_display} paper: {question}")
    
    try:
        paper = ai.generate(prompt, system_prompt, max_tokens=8192)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        lang_code = "zh" if language == "chinese" else "en"
        paper_id = f"apep_{timestamp}_{lang_code}"
        
        papers_dir = Path(__file__).parent.parent / "papers"
        papers_dir.mkdir(exist_ok=True)
        
        filepath = papers_dir / f"{paper_id}.md"
        with open(filepath, 'w') as f:
            f.write(f"# {question}\n\n")
            f.write(f"**Language:** {lang_display}\n")
            f.write(f"**Field:** {field}\n")
            f.write(f"**Method:** {method if method else 'DiD'}\n")
            f.write(f"**ID:** {paper_id}\n")
            if data_path:
                f.write(f"**Data Source:** {data_path}\n")
            if refs_path:
                f.write(f"**References:** {refs_path}\n")
            f.write("\n---\n\n")
            f.write(paper)
        
        print(f"✅ {lang_display} paper saved: {filepath}")
        print(f"   ID: {paper_id}")
        return paper_id
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_paper.py 'Question' [field] [method] [data_path] [refs_path] [language]")
        print("")
        print("Language: english (default) or chinese")
        sys.exit(1)
    
    question = sys.argv[1]
    field = sys.argv[2] if len(sys.argv) > 2 else "economics"
    method = sys.argv[3] if len(sys.argv) > 3 else ""
    data_path = sys.argv[4] if len(sys.argv) > 4 else None
    refs_path = sys.argv[5] if len(sys.argv) > 5 else None
    language = sys.argv[6] if len(sys.argv) > 6 else "english"
    
    generate_paper(question, field, method, data_path, refs_path, language)
