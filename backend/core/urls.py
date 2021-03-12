from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path("", views.api_root),
    path("core/", views.MaterialList.as_view(), name="material-list"),
    path("core/<int:pk>/", views.MaterialDetail.as_view()),
    path("auth/users/", views.UserList.as_view(), name="user-list"),
    path("auth/users/<int:pk>", views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)