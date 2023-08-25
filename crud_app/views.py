from django.shortcuts import redirect, render
# from .forms import *
from .models import *

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        roll = request.POST['roll']
        section = request.POST['section']
        Student(name=name,
                email=email,
                roll_number = roll,
                section =section).save()
        return redirect('create')

    data = Student.objects.all()
    return render(request,'index.html',{'data':data})

def edit(request,id):
    dataget = Student.objects.get(id = id)
    data = Student.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        roll = request.POST['roll']
        section = request.POST['section']
        dataget.name = name
        dataget.email = email
        dataget.roll_number = roll
        dataget.section = section
        dataget.save()
        return redirect('create')
    return render(request,'index.html',{'dataget':dataget,'data':data})

def delete(request,id):
    dataget = Student.objects.get(id=id)
    dataget.delete()
    return redirect('create')




