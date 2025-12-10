from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form, name='student_form'),
    path('list/', views.student_list, name='student_list'),
    path('student/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
]
