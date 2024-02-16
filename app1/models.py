from django.db import models

class CalculatedResult(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    result = models.FloatField()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_id}"    