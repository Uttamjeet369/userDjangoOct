from django.urls import path

from . import views

urlpatterns = [
    path('user_signup/', views.signup, name='user_signup'),
    path('user_login/', views.login, name='user_login'),
]