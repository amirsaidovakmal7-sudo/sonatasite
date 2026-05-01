from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('try-free-lesson', views.free_lesson),

]