from django.shortcuts import render,get_object_or_404
from operation.models import opr

from django.http import HttpResponse

def home(request):
    data=opr.objects.all()
    context={'data':data}
    return render(request,'index.html',context)


