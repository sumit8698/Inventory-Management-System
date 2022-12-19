from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'UserApp'
urlpatterns = [
    path('Register', views.register, name='Register'),
    path('user-login', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('user-logout', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('userprofile_update', views.userprofile_update, name="userprofile_update")
]
