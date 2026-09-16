from django.urls import path
from . import views

urlpatterns = [
    #create and fetch(all)
    path('students/', views.studentsView) ,
    #fetch(one)
    path('students/<int:pk>/', views.studentDetailsView)
]