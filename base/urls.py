from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<str:title>', views.subject, name='subject'),
]
