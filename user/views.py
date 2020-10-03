from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from user.forms import RegisterForm

# Create your views here/.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    return render(request, 'main/home.html',{'Main': Main.objects.filter(RegisterNumber = id).first()})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username ,password=password)
        if user is not None:
            login_user(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,'user/user.html', {
            'message':'Invalid Credentials'
            })
    return render(request,'user/user.html')


def register(request):
    f = RegisterForm()
    m = NameForm()

    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
        m = NameForm(request.POST)
        
        obj = m.save(commit=False)
        obj.RegisterNumber = request.POST['username']
        print(request.POST['username'])

        if m.is_valid():
            print("hii")
            obj.save()

        
            return HttpResponseRedirect(reverse("login"))
    return render(request,"user/register.html",{
        "form":f , "name" : m
    })


def status(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    return render(request,'main/nav.html',{'Main': Main.objects.filter(RegisterNumber = id).first()})


def sem1(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem1.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
        "Sem1" : Data[0],"message":"sem1",'Main': Main.objects.filter(RegisterNumber = id).first()
        })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })
def sem2(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem2.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
        "Sem2" : Data[0],"message":"sem2",'Main': Main.objects.filter(RegisterNumber = id).first()
        })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })    

def sem3(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem3.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
    "Sem3" : Data[0],"message":"sem3",'Main': Main.objects.filter(RegisterNumber = id).first()
    })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })



def sem4(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem4.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
    "Sem4" : Data[0],"message":"sem4",'Main': Main.objects.filter(RegisterNumber = id).first()
    })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })


def sem5(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem5.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
    "Sem5" : Data[0],"message":"sem5",'Main': Main.objects.filter(RegisterNumber = id).first()
    })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })


def sem6(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem6.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
    "Sem6" : Data[0],"message":"sem6",'Main': Main.objects.filter(RegisterNumber = id).first()
    })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })


def sem7(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem7.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
    "Sem7" : Data[0],"message":"sem7",'Main': Main.objects.filter(RegisterNumber = id).first()
    })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })


def sem8(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    id = request.user.username
    Data = Sem8.objects.filter(id= id)
    try:
        return render(request, "main/sem1.html", {
    "Sem8" : Data[0],"message":"sem8",'Main': Main.objects.filter(RegisterNumber = id).first()
    })
    except IndexError :
        return render(request,"main/sem1.html",{
            "Error":"No Records Found."
        })
def update1(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem1form()

    
    if request.method == "POST":

        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem1form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()
        return render(request,"main/update.html",{
    "form":form,"message":"sem1","alert":"Your Grades Are Updated Successfully."
    })
        

    return render(request,"main/update.html",{
    "form":form,"message":"sem1"
    })


def update2(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem2form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem2form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()

        return render(request,"main/update.html",{
    "form":form,"message":"sem2","alert":"Your Grades Are Updated Successfully."
    })

    return render(request,"main/update.html",{
    "form":form,"message":"sem2"
    })


def update3(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem3form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem3form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()

        return render(request,"main/update.html",{
    "form":form,"message":"sem3","alert":"Your Grades Are Updated Successfully."
    })
    return render(request,"main/update.html",{
    "form":form,"message":"sem3"
    })


def update4(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem4form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem4form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()
        return render(request,"main/update.html",{
    "form":form,"message":"sem4","alert":"Your Grades Are Updated Successfully."
    })
    
    return render(request,"main/update.html",{
    "form":form,"message":"sem4"
    })


def update5(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem5form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem5form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()

        return render(request,"main/update.html",{
    "form":form,"message":"sem5","alert":"Your Grades Are Updated Successfully."
    })
    return render(request,"main/update.html",{
    "form":form,"message":"sem5"
    })


def update6(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem6form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem6form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()
        return render(request,"main/update.html",{
    "form":form,"message":"sem6","alert":"Your Grades Are Updated Successfully."
    })

        

    return render(request,"main/update.html",{
    "form":form,"message":"sem6"
    })


def update7(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem7form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem7form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()
        return render(request,"main/update.html",{
    "form":form,"message":"sem7","alert":"Your Grades Are Updated Successfully."
    })

    return render(request,"main/update.html",{
    "form":form,"message":"sem7"
    })


def update8(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    id = request.user.username

    form = Sem8form()

    
    if request.method == "POST":
        main_obj=Main.objects.get(RegisterNumber=id)

        form = Sem8form(request.POST)
       
        obj_form=form.save(commit=False)
        obj_form.id=main_obj
        obj_form.save()

        return render(request,"main/update.html",{
    "form":form,"alert":"Your Grades Are Updated Successfully.","message":"sem8"
    })


    return render(request,"main/update.html",{
    "form":form,"message":"sem8"
    })



def logout(request):
    logout_user(request)
    return HttpResponseRedirect(reverse('login'))
    
