from django.urls import path
from ml import views

urlpatterns = [
    path("", views.PreView.as_view()),
    path("sim/<int:mat_pk>/", views.SimAnalysisView.as_view()),
]