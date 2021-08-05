from django.db import models
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    ssal=models.FloatField()
    saddr=models.CharField(max_length=30)
