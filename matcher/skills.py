import re
from io import BytesIO
from pypdf import PdfReader

# Extend this list for your course or target job domain.
SKILLS = [
    "python", "java", "javascript", "typescript", "c++", "c#", "sql",
    "django", "flask", "fastapi", "react", "angular", "vue", "node.js",
    "html", "css", "bootstrap", "rest api", "graphql", "git", "github",
    "linux", "docker", "kubernetes", "aws", "azure", "gcp", "postgresql",
    "mysql", "sqlite", "mongodb", "redis", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "natural language processing", "nlp", "power bi", "tableau", "excel",
    "data structures", "algorithms", "object-oriented programming", "oop",
    "unit testing", "pytest", "selenium", "agile", "scrum", "communication",
    "problem solving", "project management", "figma", "ui/ux", "cybersecurity",
]

def extract_pdf_text(file_obj):
    """Extract text from a PDF. Scanned/image-only PDFs may return no text."""
    data = file_obj.read()
    reader = PdfReader(BytesIO(data))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return "\n".join(pages).strip()

def contains_skill(text, skill):
    # Case-insensitive whole-ish phrase match; avoids matching 'java' inside 'javascript'.
    escaped = re.escape(skill.lower())
    pattern = r"(?<![a-z0-9])" + escaped + r"(?![a-z0-9])"
    return re.search(pattern, text.lower()) is not None

def find_skills(text):
    return sorted([skill for skill in SKILLS if contains_skill(text, skill)])

def analyze_match(resume_text, job_description):
    job_skills = find_skills(job_description)
    resume_skills = find_skills(resume_text)
    # Score only against skills explicitly detected in the job description.
    if job_skills:
        matched = [skill for skill in job_skills if skill in resume_skills]
        missing = [skill for skill in job_skills if skill not in resume_skills]
        score = round((len(matched) / len(job_skills)) * 100)
    else:
        matched, missing, score = [], [], 0

    if not job_skills:
        recommendation = (
            "No skills from the built-in skill dictionary were detected in the job description. "
            "Add specific technical or professional skills, or expand matcher/skills.py."
        )
    elif score >= 80:
        recommendation = "Strong keyword overlap. Review the job requirements and make sure your resume gives evidence for each matched skill."
    elif score >= 50:
        recommendation = "Moderate keyword overlap. Add truthful project or coursework evidence for relevant missing skills, if you have them."
    else:
        recommendation = "Low keyword overlap. Compare the job requirements with your experience and make a learning plan for the gaps."
    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": score,
        "recommendation": recommendation,
    }
