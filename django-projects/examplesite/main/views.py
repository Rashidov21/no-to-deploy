from django.shortcuts import render

# Create your views here.


def homePageView(request):
    numbers = list(range(10))
    data = {
        'header': "Django template test view",
        "content": "This is text content.",
        "numbers": numbers
    }
    return render(request, "index.html", context=data)
