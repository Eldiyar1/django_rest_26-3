from django.urls import path
from .views import AuthorizationAPIView, RegistrationAPIView
urlpatterns = [
    path('authorization/', AuthorizationAPIView.as_view()),
    path('registration/', RegistrationAPIView.as_view())
]
