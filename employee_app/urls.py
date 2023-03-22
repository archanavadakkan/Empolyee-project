from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee,name='employee'),
    path('EmployeeData/<int:emp_id>',views.employeeDetail,name='detail'),
    path('add/',views.add_employee,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]