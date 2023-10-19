from django.test import TestCase
from .models import Student, Performance
from .forms import StudentForm
from .analysis import perform_analysis
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import Client


# Create your tests here.
class StudentTestCase(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(name='Ilham', age=20, gender='Male', gpa=3.5)
        self.assertEqual(student.name, 'Ilham')