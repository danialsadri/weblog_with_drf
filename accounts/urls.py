from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit/user/', views.EditUserView.as_view(), name='edit_user'),
    path('login/', obtain_auth_token, name='login'),
]
