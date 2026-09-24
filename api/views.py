from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer, BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http  import Http404
from rest_framework.exceptions import NotFound
from rest_framework import mixins, generics
from rest_framework import viewsets
from blogs.models import Blog, Comment
from .paginations import CustomPageNumberPagination, CustomLimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter


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

#         paginator = CustomPageNumberPagination()

#         #main logic conn.
#         page = paginator.paginate_queryset(employees, request, view=self)


#         serializer = EmployeeSerializer(page, many=True)
#         return paginator.get_paginated_response(serializer.data) 
#         # return Response(serializer.data, status=status.HTTP_200_OK)

    

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


"""
#Mixins
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

#Mixins
class EmployeeDetails(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk) 

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

"""


"""
#Generics
class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



#Generics 
class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

"""

"""
#views.ViewSet
class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        employee = get_object_or_404(Employee, pk = pk)
        return employee
    
    def retrieve(self, request, pk=None):
        employee=self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        employee=self.get_object(pk)
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""




#viewset.ModelViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['designation']
    filterset_class = EmployeeFilter
    filter_backends = [OrderingFilter]
    ordering_fields = ['emp_id']





# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all() 
#     serializer_class = BlogSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all() 
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['comments__comment', 'blog_title', 'blog_body']
    ordering_fields = ['pk']

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

