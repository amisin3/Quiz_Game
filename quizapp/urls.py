from django.urls import re_path
from . import views

app_name = 'quizapp'

urlpatterns = [
    re_path(r'^list', views.Quiz.as_view(), name='list'),
    re_path(r'^detail/(?P<pk>\d+)',
            views.QuizDetailView.as_view(), name='detail'),
    re_path(r'choice/(?P<pk>\d+)', views.choice, name='choice'),
    re_path(r'results/', views.ResultsView.as_view(), name='results'),
    re_path(r'^$', views.list_page, name='list'),
    re_path(r'^hello/', views.create_list, name='hello'),
    re_path(r'^create/(?P<pk>\d+)', views.create_test_view, name='create'),
]
