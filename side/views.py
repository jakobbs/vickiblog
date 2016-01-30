from django.shortcuts import render
from django.utils import timezone
from .models import Project


def projecter(request):
    proj = Project.objects.all()	
   
    return render(request, 'side/forside.html', {'projecter': proj })
