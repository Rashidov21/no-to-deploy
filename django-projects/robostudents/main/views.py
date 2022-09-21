from django.shortcuts import render
from .models import Student, Course
# Create your views here.


def all_students(request):
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})
