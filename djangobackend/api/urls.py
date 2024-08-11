from django.contrib import admin
from django.urls import path,include
from api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'stu', views.StudentViewset, basename='user')

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('studentc/', views.StudentCreate.as_view()),
    path('studentr/<int:pk>/', views.StudentRetrive.as_view()),
    path('studentu/<int:pk>/', views.StudentUpdate.as_view()),
    path('studentd/<int:pk>/', views.StudentDestroy.as_view()),
    path('', include(router.urls))
]
