from django.shortcuts import render, redirect
from django.contrib import messages


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
    # object_list = Student.objects.filter(name__exact="Marcus Rashford") # bir xil bo'lsa
    # object_list = Student.objects.filter(name__istartswith="mar") # Marcus Rashford

    # name__iexact="Marcus Rashford"  bir xil bo'lsa harf katta kichikligini farqi yo'q
    # name__contains="Marcus"  jumla mavjud bo'lsa 
    # name__icontains="marc"  jumla mavjud bo'lsa harf katta kichikligini farqi yo'q
    
    # print(object_list) # <QuerySet [<Student: Marcus Rashford>]>
    
    # Create new objects 
    # Stacks.objects.create(name='UI/UX', stars=8)
    # print("OK")
    # Update some object
    # temp = Stacks.objects.get(name="UI/UX")
    # temp.stars = 9
    # temp.save()
    # print("OK")
    
    # Create new object with HTML form 

        
        
    
    
    stacks = Stacks.objects.all()
    # stacks = Stacks.objects.filter(stars__gte=5)
    # stacks = Stacks.objects.filter(stars__range=5) # 0 dan  5 gacha qiymatlarni olish
    # stacks = Stacks.objects.filter(stars__in=[5,9]) # 5 yoki 9 ta yulduzi borlar
    course = Course.objects.all()
    data = {
        "stacks":stacks,
        "courses":course
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
        # data = Student.objects.filter(age__lt=int(query)) # lt - dan kichik 
        # data = Student.objects.filter(age__lte=int(query)) # lte - ga teng yoki kichik 
        # data = Student.objects.filter(age__gt=int(query)) # gt - dan katta
        # data = Student.objects.filter(age__gte=int(query)) # gte - ga teng yoki  katta 
        if data:
            return render(request, "index.html", context={"object_list":data})
        else:  
            return render(request, "index.html", context={"message":"Result not found !"})

        
    
    return render(request, "index.html")




def add_course_view(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        if len(name) < 3:
            messages.add_message(request, messages.INFO, "Course name too short !")
        else:
            Course.objects.create(name=name)
            messages.add_message(request, messages.SUCCESS, "New course object added !")
    else:
        messages.add_message(request, messages.ERROR, "Something went wrong !")
        
    return redirect("/")
