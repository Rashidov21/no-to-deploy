from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question
# Create your views here.


def home(request):
    question = Question.objects.all()
    context = {
        'questions': question
    }
    return render(request, 'index.html', context)


def results(request, quest_id):
    # print(request.GET.get('answer'))
    question = Question.objects.get(id=quest_id)
    right_answer = question.right_answer
    # print(type(request.GET.get('answer')))
    # print(type(right_answer))
    if int(request.GET.get('answer')) == right_answer:
        messages.add_message(request, messages.SUCCESS, "To'g'ri toptiz !")
    else:
        messages.add_message(request, messages.ERROR, "Xato javob !")

    return redirect("main:home")


def contact(request):
    return render(request, 'contact.html')
