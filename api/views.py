from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http  import Http404
from rest_framework.exceptions import NotFound
from rest_framework import mixins, generics

# Create your views here.


@api_view(['GET' ,'POST'])
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
    elif request.method == "POST" : 
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else : 
            print(serializer.errors)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailsView(request, pk):
    student = get_object_or_404(Student, pk = pk)

    if request.method == "GET" : 
        serializer = StudentSerializer(student)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == "PUT" : 
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE" : 
        print(StudentSerializer(student).data) 
        student.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)


# class Employees(APIView):
#     #method like a fn based view , get method check is already there
#     def get(self, request):
#         employees = Employee.objects.all() 
#         serializer = EmployeeSerializer(employees, many=True) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetails(APIView):

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk): #elif request.method == "DELETE":
#         employee = self.get_object(pk)
#         print("DELETED USER : ",EmployeeSerializer(employee).data)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class Employees(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request):  
        return self.list(request)

    def post(self, request):
        return self.create(request)

class EmployeeDetails(generics.GenericAPIView):
    pass