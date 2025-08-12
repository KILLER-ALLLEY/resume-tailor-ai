import pdfplumber
import re

def clean_resume_text(text):
    lines = text.split('\n')
    filtered_lines = []
    seen = set()
    for line in lines:
        line_strip = line.strip()
        if line_strip and line_strip not in seen:
            filtered_lines.append(line)
            seen.add(line_strip)

    text = '\n'.join(filtered_lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    return text.strip()

def extract_resume_text(pdf_path):
    resume_text = ""  
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  
                resume_text += page_text + "\n"

    return clean_resume_text(resume_text)
