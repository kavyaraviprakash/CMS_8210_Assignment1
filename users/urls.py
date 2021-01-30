from django.urls import path
from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.urls import re_path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
