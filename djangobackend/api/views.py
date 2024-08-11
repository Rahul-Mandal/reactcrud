from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# viewsets based

class StudentViewset(viewsets.ViewSet):
    def list(self,request):

        queryset = Student.objects.all()
        serializer_data = StudentSerializer(queryset, many=True)
        return Response(serializer_data.data)
    
    def retrieve(self, request, pk=None):
        id = pk
        print(id)
        if id is not None:
            st = Student.objects.get(id=id)
            serializer_data = StudentSerializer(st)
            return Response(serializer_data.data)
    
    def create(self, request):
        serial_Data = StudentSerializer(data=request.data)
        if serial_Data.is_valid():
            serial_Data.save()
            return Response({'msg':'Data_created'},status=status.HTTP_201_CREATED)
        return Response(serial_Data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk):
        print(pk)
        id = pk
        stu = Student.objects.get(id=id)
        ser = StudentSerializer(stu, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Updated'})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        stu = Student.objects.get(pk=pk)
        ser = StudentSerializer(stu, data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Partially Updated'})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,pk,request):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Deleted'})