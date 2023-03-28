from django.shortcuts import render,redirect
#from .models import *
from .models import Candidate,Vacancy
#from django.contrib.auth.forms import UserCreationForm
#from users.forms import UserCreationForm
from users.forms import CustomUserCreationForm,RecruiterCreationForm,SeekerCreationForm
from django.contrib.auth import login,logout,authenticate
#from .forms import *
from .forms import ApplyForm

# Create your views here.
def seekerReg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=SeekerCreationForm()
        if request.method=='POST':
            Form=SeekerCreationForm(request.POST)
            print(Form.errors)
            if Form.is_valid():
                Form.save()
                return redirect('login')
        context={
            'form':Form
        }
    return render(request,'seekerReg.html',context)

def recruiterReg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=RecruiterCreationForm()
        if request.method=='POST':
            Form=RecruiterCreationForm(request.POST)
            print(Form.errors)
            if Form.is_valid():
                Form.save()
                return redirect('login')
        context={
            'form':Form
        }
    return render(request,'recruiterReg.html',context)

def home(request):
    if request.user.is_authenticated:
        if request.user.user_type =="Recruiter":
            candidate=Candidate.objects.filter(vacancy__user_id=request.user.id)
            context={
            'candidate':candidate,
            }
            return render(request,'Jobseeker.html',context)
        else:
            vacancies=Vacancy.objects.all()
            context={
                'vacancies':vacancies,
                }
            return render(request,'Jobseeker.html',context)
    else:
        return render(request,'home.html')



def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        user=authenticate(request,email=email,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
       return render(request,'login.html')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=CustomUserCreationForm()
        if request.method=='POST':
            Form=CustomUserCreationForm(request.POST)
            if Form.is_valid():
                Form.save()
                return redirect('login')
        context={
            'form':Form
        }
        return render(request,'register.html',context)

def applyPage(request):
    form=ApplyForm()
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'apply.html',context)