# MCA Mini Project Report
## CareerMatch: Resume Analyzer and Job Skill Matcher

### 1. Abstract
CareerMatch is a web-based application that helps students compare a resume with a target job description. The user uploads a text-based PDF resume and pastes a job description. The application extracts text, detects skills from a configurable dictionary, calculates a transparent keyword-overlap percentage, lists matched and missing skills, and stores a report for later review. The application uses Django authentication and restricts reports to their owners.

### 2. Problem statement
Students and fresh graduates may find it difficult to identify which skills in a job advertisement are represented in their resumes. Manual comparison is time-consuming, and generic resume scores may not explain how a score was produced.

### 3. Objectives
- Extract selectable text from PDF resumes.
- Identify skills from a configurable vocabulary.
- Compare resume skills with job-description skills.
- Display a transparent percentage and matched/missing skill lists.
- Preserve private analysis history for registered users.
- Provide an extensible base for future NLP-based matching.

### 4. Scope and limitations
The prototype supports text-based PDF files up to 5 MB. It uses a fixed skill dictionary and keyword overlap. It does not evaluate experience quality, infer skill proficiency, parse scanned PDFs with OCR, or make hiring decisions. A skill absent from the text may still be known by the applicant.

### 5. Technology stack
- Front end: HTML, CSS, Bootstrap 5, Django templates
- Back end: Python and Django 5.2
- Database: SQLite for a simple local setup
- PDF extraction: pypdf
- Authentication: Django built-in authentication

### 6. Main modules
1. User registration
2. User login/logout
3. Dashboard and statistics
4. PDF upload and validation
5. PDF text extraction
6. Job description input
7. Skill dictionary and detection
8. Match score calculation
9. Matched skills report
10. Missing skills report
11. Recommendations
12. Analysis history
13. Report detail view
14. Report deletion and uploaded-file cleanup
15. Django administration

### 7. Methodology
1. User uploads a PDF and provides a job title and job description.
2. The server validates extension and file size.
3. pypdf extracts selectable text from each page.
4. A configurable skill dictionary is searched in both texts using case-insensitive phrase boundaries.
5. Detected job skills are divided into matched and missing groups.
6. Match score is calculated as: (number of matched detected job skills / number of detected job skills) × 100.
7. The report is stored and shown to the authenticated owner.

### 8. Database design
ResumeAnalysis fields: id (primary key), owner (foreign key to User), resume (uploaded file path), resume_filename, job_title, job_description, extracted_text, matched_skills (JSON), missing_skills (JSON), match_percentage, recommendation, created_at.

Relationship: one user can own many ResumeAnalysis records. Deleting a user cascades to their reports.

### 9. Testing plan
- Register with valid and invalid password inputs.
- Log in with correct and incorrect credentials.
- Upload a valid text-based PDF.
- Reject a non-PDF file and a file larger than 5 MB.
- Display a helpful error for unreadable or scanned PDFs without selectable text.
- Check known skills appear as matched when present in both texts.
- Check job skills absent from the resume appear as missing.
- Confirm a report cannot be opened or deleted by another user.
- Confirm report deletion also removes its uploaded file.
- Verify dashboard counts and average score.

### 10. Evaluation metrics
- PDF extraction success rate on a small test set
- Precision/recall of skill detection against manually labelled examples
- Correctness of match-score calculation
- Response time for typical resume sizes
- Usability feedback from student testers
- Access-control test pass rate

### 11. Future enhancements
- OCR for scanned resumes
- Editable skill dictionary and domain-specific vocabularies
- Synonym normalization (e.g. PostgreSQL and SQL)
- TF-IDF or sentence-embedding similarity with explainable evidence
- Export report to PDF
- Resume version comparison
- Job listings and saved target roles
- Privacy controls and configurable retention
- Unit tests and deployment with HTTPS

### 12. Ethical considerations
Resume contents are personal data. Keep test files fictional or consented, restrict access, avoid public deployment with development settings, and delete files when no longer needed. Do not treat keyword scores as objective measures of a person's capability.
