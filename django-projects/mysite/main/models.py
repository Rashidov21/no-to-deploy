from django.db import models

# Create your models here.


class Question(models.Model):
    # savol - oddiy matnli maydon 
    question = models.TextField()
    # javoblar char , belgilar qabul qilivchi maydon
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    # to'gri javob raqami musbat son
    right_answer = models.PositiveIntegerField(default=0)

    # savol obyektiga murojaat vaqti savol matni qaytadi
    def __str__(self):
        return str(self.question)
