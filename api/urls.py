from django.urls import path
from . import views

urlpatterns = [
    #STUDENT
    #create and fetch(all)
    path('students/', views.studentsView) ,
    #fetch(one)
    path('students/<int:pk>/', views.studentDetailsView), 

    #EMPLOYEE
    #create and fetch(all)
    path('employees/', views.Employees.as_view()), 
    #fetch , edit, delete (one)
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()), 
]