from django.urls import re_path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'


urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
]