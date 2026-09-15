from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def studentsView(request):
#My MANUAL Dict Method
    # # SAFE = True
    # data = Student.objects.all()
    # students = dict()
    # for student in data: 
    #     students[student.student_id] = {
    #         'name' : student.name, 
    #         'branch' : student.branch
    #     }





    # #OFFICIAL METHOD 1
    # #SAFE = False 
    # data = Student.objects.all()
    # students_list = list()
    # for student in data: 
    #     s = {
    #     'id' : student.student_id, 
    #     'name' : student.name, 
    #     'branch' : student.branch
    #     }
    #     students_list.append(s)
    
    # #OFFICIAL METHOD 2
    # students = Student.objects.all()
    # print(students.values())
    # students_list = list(students.values())


    #OFFICIAL METHOD 3 (BEST METHOD) 

    if request.method == "GET" : 
        #get all the data from Student table 
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True) 
        # return JsonResponse(serializer.data, safe = False)
        return Response(serializer.data, status = status.HTTP_200_OK)


    # return JsonResponse(students_list, safe=False) 
