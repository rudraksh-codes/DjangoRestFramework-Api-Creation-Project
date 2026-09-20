from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')
# router.register('blogs', views.BlogViewSet, basename='blog')
# router.register('comments', views.CommentViewSet, basename='view')

urlpatterns = [
    #STUDENT
    #create and fetch(all)
    path('students/', views.studentsView) ,
    #fetch(one)
    path('students/<int:pk>/', views.studentDetailsView), 


    path('', include(router.urls)), 

    path('blogs/', views.BlogsView.as_view()), 
    # path('blogs/<int:pk>', views.BlogDetailsView.as_view()), 
    path('comments/', views.CommentsView.as_view()), 
    # path('comments/<int:pk>', views.CommentDetailsView.as_view()), 


    # #EMPLOYEE
    # #create and fetch(all)
    # path('employees/', views.Employees.as_view()), 
    # #fetch , edit, delete (one)
    # path('employees/<int:pk>/', views.EmployeeDetails.as_view()), 

  

]