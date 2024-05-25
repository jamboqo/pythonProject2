from django.urls import path
from . import views
from .views import works_home
urlpatterns = [
    path('', views.works_home, name='works_home')
]