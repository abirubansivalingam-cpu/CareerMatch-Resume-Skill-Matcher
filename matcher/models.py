from django.conf import settings
from django.db import models

class ResumeAnalysis(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resume_analyses")
    resume = models.FileField(upload_to="resumes/%Y/%m/")
    resume_filename = models.CharField(max_length=255)
    job_title = models.CharField(max_length=150, default="Target role")
    job_description = models.TextField()
    extracted_text = models.TextField(blank=True)
    matched_skills = models.JSONField(default=list, blank=True)
    missing_skills = models.JSONField(default=list, blank=True)
    match_percentage = models.PositiveSmallIntegerField(default=0)
    recommendation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.job_title} — {self.owner}"
