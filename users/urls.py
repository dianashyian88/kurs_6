from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, EmailVerify, MyLoginView, \
    MyPasswordResetView, MyPasswordResetDoneView, MyPasswordResetConfirmView, MyPasswordResetCompleteView
from django.views.generic import TemplateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'),
         name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'),
         name='invalid_verify'),
    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
