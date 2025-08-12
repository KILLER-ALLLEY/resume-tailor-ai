from openai import OpenAI
from resume_extraction import extract_resume_text
import json
import re


pdf_path = r"C:\Users\srina\Resume\resume-tailor-ai\Srinath.K Resume.pdf"
resume_text = extract_resume_text(pdf_path)



# Read API key from file
with open(r"C:\Users\srina\Resume\resume-tailor-ai\api_key.txt", "r") as file:
    api_key = file.read().strip()


job_description=f"""

Job Title: Data Analyst
Location: Remote / Bangalore, India
Job Summary:
We are seeking a detail-oriented Data Analyst to join our team. The ideal candidate will have strong analytical skills and experience working with large datasets to help drive business decisions.

Responsibilities:
Collect, clean, and analyze large datasets from multiple sources.
Create reports, dashboards, and visualizations to communicate insights to stakeholders.
Collaborate with cross-functional teams to identify business opportunities and improve processes.
Use statistical techniques to interpret data and provide actionable recommendations.
Automate repetitive data tasks and improve data quality.

Requirements:
Bachelor’s degree in Statistics, Mathematics, Computer Science, or related field.
Proficiency in SQL and Excel.
Experience with data visualization tools such as Tableau, Power BI, or Looker.
Strong knowledge of Python or R for data analysis.
Familiarity with statistical methods and data modeling.
Excellent communication and problem-solving skills.
Ability to work independently and in a team environment.

Preferred:
Experience with cloud platforms like AWS or GCP.
Knowledge of machine learning basics.
Experience with big data technologies (e.g., Hadoop, Spark).

"""


prompt=f""" 
Compare the following resume and job description, and return ONLY valid JSON with the following keys:
- match_score: integer from 0 to 100
- missing_skills: list of skills not present in resume but in JD
- strengths: list of relevant strengths found in resume
- weaknesses: list of weaknesses or gaps

Resume:
\"\"\"{resume_text}\"\"\"

Job Description:
\"\"\"{job_description}\"\"\"

Return ONLY JSON. No explanations, no extra text.
"""

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",temperature=0,
    messages=[
        {"role": "system", "content": "You are a JSON-only generator. Always return valid JSON without any extra text."},
        {"role": "user", "content": prompt}
    ]
)


raw_output = completion.choices[0].message.content.strip()
try:
    result = json.loads(raw_output)
except json.JSONDecodeError:
    # Fallback if LLM adds extra text accidentally
    import re
    match = re.search(r"\{.*\}", raw_output, re.DOTALL)
    if match:
        result = json.loads(match.group(0))
    else:
        raise ValueError("No valid JSON found in LLM output.")
    
print("Match Score:", result.get("match_score", 0))
print("Missing Skills:")
for skill in result.get("missing_skills", []):
    print(" -", skill)

print("\nStrengths:")
for strength in result.get("strengths", []):
    print(" -", strength)

print("\nWeaknesses:")
for weakness in result.get("weaknesses", []):
    print(" -", weakness)