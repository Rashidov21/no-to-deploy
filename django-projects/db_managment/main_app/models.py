from django.db import models

# Create your models here.

class Stacks(models.Model):
    name = models.CharField(max_length=100)
    stars = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return str(self.name)
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.name)
    

