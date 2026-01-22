from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def index(request):
    if request.method== "POST":
        nm=request.POST['name']
        e=request.POST['email']
        mob=request.POST['mobile']
        s=request.POST['salary']
        p=request.POST['position']
        print(nm,e,mob,s,p)

        obj=Employee.objects.create(name=nm,email=e,mobile=mob,salary=s,position=p)
        obj.save()
        # return HttpResponse("Form Submitted successfully!")
    return render(request,'index.html')

def table(request):
    emp=Employee.objects.all()
    print(emp)
    context={}
    context["emp"]=emp
    for i in emp:
        print(i.name,i.email,i.mobile,i.salary,i.position)
    return render(request,'table.html',context)

def delete(request,e_id):
    emp=Employee.objects.get(id=e_id)
    print(emp.name)
    emp.delete()
    return redirect('/table')

def edit(request,e_id):
    context={}
    if request.method == "GET":
        emp=Employee.objects.get(id=e_id)
        context["emp"]=emp
        return render(request,'edit.html',context)
    elif request.method == "POST":
        nm=request.POST['name']
        e=request.POST['email']
        mob=request.POST['mobile']
        s=request.POST['salary']
        p=request.POST['position']
        emp1=Employee.objects.filter(id=e_id)
        emp1.update(name=nm,email=e,mobile=mob,salary=s,position=p)
        return redirect('/table')
        


