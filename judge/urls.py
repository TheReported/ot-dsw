from django.urls import path

from . import views

app_name = 'judge'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<slug:slug>/', views.judge_detail, name='detail'),
]
