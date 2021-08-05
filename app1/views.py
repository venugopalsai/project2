from django.shortcuts import render
from app1.models import Employee 
# Create your views here.
def sample(request):
    p1=Employee.objects.create(eno=5,ename='pooja',esal=50000,eaddr='gudivada')
    p1.save()
    res = Employee.objects.all()
    return render(request,'sample.html',{'res':res})
