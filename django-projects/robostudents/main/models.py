from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    PAYMENT = (
        ("NAQD", 'naqd'),
        ("PLASTIK", 'plastik'),
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='students/')
    brithday = models.DateField()
    payment_method = models.CharField(choices=PAYMENT, max_length=30)

    def __str__(self):
        return str(self.name)
