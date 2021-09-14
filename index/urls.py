from django.urls import path

from . import views


app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:health_id>/', views.lists, name='lists'),
]
