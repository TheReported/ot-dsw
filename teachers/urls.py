from django.urls import path

from . import views

app_name = 'teachers'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<slug:slug>/', views.teacher_detail, name='detail'),
]
