from django.shortcuts import render
from .models import Login
from .serializer import LoginSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import requests

from .models import Register
from .serializer import RegisterSerializer

# Create your views here.
def login(request):       
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')               
        Visitlll = Login(username=username, password=password)                         
        Visitlll.save()


    # data = {
    #     "title": "Home Page",
    #     "description": "BAAP AGRO!!!"
    # }3
    return render(request,'login.html')



def login_detail(request, pk):
    stu = Login.objects.get(id = pk)
    serializer = LoginSerializer(stu)    
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Login.objects.all()
    serializer = LoginSerializer(stu, many = True)    
    return JsonResponse(serializer.data, safe = False)

def VisitData(request):
    URL = "http://127.0.0.1:8000/list/"
    r = requests.get(url=URL)
    data = r.json()
    return render(request, 'displaylogin.html', {'response':data}) 




def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')               
        username = request.POST.get('username')           
                     
        mobile = request.POST.get('mobile')               
        email = request.POST.get('email')               
        address = request.POST.get('address')               
        Visitlll = Register(firstname=firstname, lastname=lastname,username=username, mobile=mobile, email=email,address=address )                         
        Visitlll.save()

    return render(request, 'register.html')



def register_detail(request, pk):
    stu = Register.objects.get(id = pk)
    serializer = RegisterSerializer(stu)    
    return JsonResponse(serializer.data)

def register_list(request):
    stu = Register.objects.all()
    serializer = RegisterSerializer(stu, many = True)    
    return JsonResponse(serializer.data, safe = False)

def registerData(request):
    URL = "http://127.0.0.1:8000/list1/"
    r = requests.get(url=URL)
    data = r.json()
    return render(request, 'displayregister.html', {'response':data}) 