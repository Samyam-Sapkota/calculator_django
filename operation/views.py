from django.shortcuts import render,get_object_or_404,redirect

from django.http import HttpResponse
from .models import opr
from .DMAS import addi,subt,mult,divi



# def scan_number(request):
#     read_number1=request.POST['f_num']
#     read_number2=request.POST['s_num']
    
def addison(request):
    read_number1=int(request.POST['f_num'])
    read_number2=int(request.POST['s_num'])
    # read_number1=request.POST['f_num']            If not kept integer it will concatinate 
    # read_number2=request.POST['s_num']
    calculation=addi(read_number1,read_number2)
    
    opr.objects.create(int_a=read_number1,int_b=read_number2,result=calculation,algebra='+')
    return redirect('home')
    
def subtraction(request):
    read_number1=int(request.POST['f_num'])
    read_number2=int(request.POST['s_num'])
    calculation=subt(read_number1,read_number2)
    
    opr.objects.create(int_a=read_number1,int_b=read_number2,result=calculation,algebra='-')
    return redirect('home')

def multiplication(request):
    read_number1=int(request.POST['f_num'])
    read_number2=int(request.POST['s_num'])
    calculation=mult(read_number1,read_number2)
    
    opr.objects.create(int_a=read_number1,int_b=read_number2,result=calculation,algebra='*')
    return redirect('home')

def divison(request):
    read_number1=int(request.POST['f_num'])
    read_number2=int(request.POST['s_num'])
    calculation=divi(read_number1,read_number2)
    
    opr.objects.create(int_a=read_number1,int_b=read_number2,result=calculation,algebra='/')
    return redirect('home')
