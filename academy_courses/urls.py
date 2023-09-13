from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('courses/', views.course, name='course'),
    path('courses/<int:pk>/', views.course_list, name='course_list'),
    path('courses/show/<int:pk>/', views.CourseDetailView.as_view(), name='course_page'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create')
]