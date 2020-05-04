from django.urls import path
from release import views

app_name = 'release'
urlpatterns = [
    path('add/', views.add, name='add'),
]