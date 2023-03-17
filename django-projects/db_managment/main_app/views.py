from django.shortcuts import render

# Create your views here.


def testView(request):
    # your db managment is here
    
    
    data = {
        
    }
    return render(request, "index.html", context=data)