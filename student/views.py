from django.shortcuts import render
from .models import Classes,Level
from django.views.generic import ListView ,DetailView

# Create your views here.
def post_list(request):
    objects=Level.objects.all()
        
    return render(request,'classes.html',{"Level":objects})
    
def B(request):
    objects=Classes.objects.all()   
    return render(request,'classes.html',{"classs":objects})
