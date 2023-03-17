from django.shortcuts import render
from .models import Stacks, Course, Student
# Create your views here.


# Django ORM 

def testView(request):
    # your db managment is here
    
    # first_stack = Stacks.objects.first() # modeldan 1-object ni olish
    # last_stack = Stacks.objects.last() # modeldan oxirgi qo'shilgan object ni olish
    
    # print(dir(first_stack))
    # print(type(first_stack))
    
    
   
    # get 
    # one_item = Course.objects.get(pk=1) # faqat 1 object olish
    # #  SELECT * FROM course WHERE id=1
    # get_one_item_by_name = Student.objects.get(name="Marcus Rashford")
    # print(one_item) #Front-End
    # print(get_one_item_by_name) #Marcus Rashford
    
    # filter 
    object_list = Student.objects.filter(name__exact="Marcus Rashford") # bir xil bo'lsa

    # name__iexact="Marcus Rashford"  bir xil bo'lsa harf katta kichikligini farqi yo'q
    # name__contains="Marcus"  jumla mavjud bo'lsa 
    # name__icontains="marc"  jumla mavjud bo'lsa harf katta kichikligini farqi yo'q
    
    print(object_list) # <QuerySet [<Student: Marcus Rashford>]>

    data = {
        "object":None
    }
    return render(request, "index.html", context=data)


def search(request):
    # print(request) #<WSGIRequest: GET '/search/'>
    # print(request.path)  # /search/
    # print(request.get_full_path())  # /search/
    # print(request.get_host())  # 127.0.0.1:8000
    # print(request.get_port()) # 8000
    # print(request.method) # GET
    
    # print(request.GET.get("q")) # input value
    # print(request.GET["q"]) # input value
    if request.method == "GET":
        
        query = request.GET.get("q")
        
        data = Student.objects.filter(name__icontains=query)
        if data:
            return render(request, "index.html", context={"object_list":data})
        else:  
            return render(request, "index.html", context={"message":"Result not found !"})

        
    
    return render(request, "index.html")