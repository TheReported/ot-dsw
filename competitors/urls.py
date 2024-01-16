from django.urls import path

from . import views

app_name = 'competitors'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('nominated/', views.competitor_nominated, name='nominated'),
    path('<slug:slug>/vote/', views.vote_competitor, name='vote'),
    path('<slug:slug>/', views.competitor_detail, name='detail'),
]
