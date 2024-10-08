from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user_signup/', views.signup, name='user_signup'),
    path('user_login/', views.login, name='user_login'),

    path('sayhello/', views.sayHello, name='sayhello'),
    path('token/refresh/', TokenRefreshView.as_view())
]