from django.urls import path, include
from .views import RegisterView, UpdateProfileView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('update/<int:pk>', UpdateProfileView.as_view()),
]