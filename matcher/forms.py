from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class AnalysisForm(forms.Form):
    resume = forms.FileField(help_text="PDF only; text-based PDFs work best.")
    job_title = forms.CharField(max_length=150, initial="Target role")
    job_description = forms.CharField(
        min_length=30,
        widget=forms.Textarea(attrs={"rows": 8, "placeholder": "Paste the job description here..."}),
        help_text="Paste the responsibilities and required skills from the job posting."
    )

    def clean_resume(self):
        f = self.cleaned_data["resume"]
        if not f.name.lower().endswith(".pdf"):
            raise forms.ValidationError("Please upload a PDF file.")
        if f.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File is too large. Maximum size is 5 MB.")
        if f.size == 0:
            raise forms.ValidationError("The uploaded file is empty.")
        return f
