from django.urls import path, include
from .views import RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordView


urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('activation/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    
]
# admin, 1 -> oijasdojif9230d232dlk




