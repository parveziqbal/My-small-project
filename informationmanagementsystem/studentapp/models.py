from django.db import models

# Create your models here.

class Student(models.Model):
    std_first_name=models.CharField(max_length=100)
    std_last_name=models.CharField(max_length=100)
    std_contact_number=models.CharField(max_length=15)
    std_email=models.EmailField()
    std_nationality=models.CharField(max_length=30)
    class Meta():
        db_table="student"


