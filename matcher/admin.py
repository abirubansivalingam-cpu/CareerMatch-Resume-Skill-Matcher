from django.contrib import admin
from .models import ResumeAnalysis

@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = ("job_title", "owner", "match_percentage", "created_at")
    list_filter = ("created_at",)
    search_fields = ("job_title", "owner__username", "resume_filename")
