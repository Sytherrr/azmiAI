from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    gpa = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'performance_analysis'


class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    attendance_choices = [
        ('Always', 'Always'),
        ('Often', 'Often'),
        ('Rarely', 'Rarely'),
    ]
    attendance = models.CharField(max_length=10, choices=attendance_choices)

    def __str__(self):
        return f"{self.student.name}'s Performance"

    class Meta:
        app_label = 'performance_analysis'
