from django.urls import path
from ml import views

urlpatterns = [
    path("", views.PreView.as_view()),
    path("sim/<int:mat_pk>/&params=<str:params>&target_results=<int:target_results>&components=<int:components>", views.SimAnalysisView.as_view()),
]