from django.db import models


# Create your models here.
class EmployeeData(models.Model):
    emp_no = models.IntegerField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    emp_start_date = models.DateField()
    emp_end_date = models.DateField()
    img = models.ImageField(upload_to='images')
    status = models.TextField()
