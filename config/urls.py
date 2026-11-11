from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from matcher import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("analyze/", views.analyze, name="analyze"),
    path("history/", views.history, name="history"),
    path("analysis/<int:pk>/", views.analysis_detail, name="analysis_detail"),
    path("analysis/<int:pk>/delete/", views.analysis_delete, name="analysis_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
