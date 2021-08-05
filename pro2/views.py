from django.shortcuts import render
from app1.models import Employee 
# Create your views here.
def student(request):
    p1=Student.objects.create(sno=5,sname='pooja',ssal=50000,saddr='gudivada')
    p1.save()
    res = Smployee.objects.all()
    return render(request,'student.html',{'res':res})
