from django.shortcuts import render,redirect
from .models import Employee


# Create your views here.
def home(request):
    return render(request,'home.html')

def Employees(request):
    return render(request,'Employees.html')

def Create(request):
    if request.method == "POST":
        id = request.POST['id']
        Name = request.POST['Name']
        DOB = request.POST['DOB']
        DOJ = request.POST['DOJ']
        Department = request.POST['Department']
        Post = request.POST['Post']
        Address =  request.POST['Address']
        City = request.POST['City']
        Country =  request.POST['Country']
        Zipcode  = request.POST['Zipcode']
        State = request.POST['State']

        Emp = Employee(id = id,Name = Name,DOB = DOB,DOJ = DOJ,Department = Department,Post = Post,Address = Address,City = City,Country = Country,Zipcode = Zipcode,State = State)
        Emp.save()
        print('user Created')
        return redirect('/')
    else:
        return render(request,"Create.html")