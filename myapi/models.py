from django.db import models

class Student(models.Model):
    stuName = models.CharField(max_length=30)
    id=models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    def __str__(self):
        return self.stuName
class Timetable(models.Model):
    date = models.DateField()
    time= models.DateTimeField()
    type = models.CharField(max_length=10)
    location = models.CharField(max_length=15)
    description =models.CharField(max_length=100)
    staff= models.CharField(max_length=50)
    def __str__(self):
        return self.date
