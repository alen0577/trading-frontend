from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def signin(request):
    return render(request,'signin.html')  

def signup(request):
    return render(request,'signup.html')       

def about(request):
    return render(request,'aboutus.html')      

def contact(request):
    return render(request,'contactus.html')      

def demat(request):
    return render(request,'demataccount.html')                  

def solution(request):
    return render(request,'solutions.html')  

def xlearn(request):
    return render(request,'xlearn.html')  


def tutorials(request):
    return render(request,'tutorials.html')                                  