from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import meet

# Create your views here.
def test(request):
    obj=place.objects.all()
    return render(request,'index.html',{'result':obj})

def demo(request):
    res=meet.objects.all()
    return  render(request,'index.html',{'key':res})