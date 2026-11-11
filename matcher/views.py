from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegisterForm, AnalysisForm
from .models import ResumeAnalysis
from .skills import extract_pdf_text, analyze_match

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "matcher/home.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Account created. You can now analyze a resume.")
        return redirect("dashboard")
    return render(request, "matcher/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    error = ""
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        error = "Invalid username or password."
    return render(request, "matcher/login.html", {"error": error})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    analyses = ResumeAnalysis.objects.filter(owner=request.user)[:5]
    all_analyses = ResumeAnalysis.objects.filter(owner=request.user)
    return render(request, "matcher/dashboard.html", {
        "analyses": analyses,
        "total_count": all_analyses.count(),
        "average_score": round(sum(a.match_percentage for a in all_analyses) / all_analyses.count()) if all_analyses.exists() else 0,
    })

@login_required
def analyze(request):
    form = AnalysisForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        uploaded = form.cleaned_data["resume"]
        try:
            text = extract_pdf_text(uploaded)
        except Exception:
            form.add_error("resume", "This PDF could not be read. Please try a valid, text-based PDF.")
        else:
            if not text.strip():
                form.add_error("resume", "No selectable text was found. This may be a scanned PDF; use a text-based PDF.")
            else:
                result = analyze_match(text, form.cleaned_data["job_description"])
                analysis = ResumeAnalysis(
                    owner=request.user,
                    resume=uploaded,
                    resume_filename=uploaded.name[:255],
                    job_title=form.cleaned_data["job_title"],
                    job_description=form.cleaned_data["job_description"],
                    extracted_text=text,
                    matched_skills=result["matched_skills"],
                    missing_skills=result["missing_skills"],
                    match_percentage=result["match_percentage"],
                    recommendation=result["recommendation"],
                )
                analysis.save()
                messages.success(request, "Resume analysis completed.")
                return redirect("analysis_detail", pk=analysis.pk)
    return render(request, "matcher/analyze.html", {"form": form})

@login_required
def history(request):
    analyses = ResumeAnalysis.objects.filter(owner=request.user)
    return render(request, "matcher/history.html", {"analyses": analyses})

@login_required
def analysis_detail(request, pk):
    analysis = get_object_or_404(ResumeAnalysis, pk=pk, owner=request.user)
    return render(request, "matcher/analysis_detail.html", {"analysis": analysis})

@login_required
def analysis_delete(request, pk):
    analysis = get_object_or_404(ResumeAnalysis, pk=pk, owner=request.user)
    if request.method == "POST":
        analysis.resume.delete(save=False)
        analysis.delete()
        messages.success(request, "Analysis deleted.")
        return redirect("history")
    return render(request, "matcher/confirm_delete.html", {"analysis": analysis})
