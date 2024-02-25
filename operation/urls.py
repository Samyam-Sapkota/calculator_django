from django.urls import path
from .models import opr
from .views import addison,subtraction,divison,multiplication

urlpatterns =[
    path('add/',addison,name="add_num"),
    path('sub/',subtraction,name="sub_num"),
    path('mult/',multiplication,name="mul_num"),
    path('div/',divison,name="div_num"),
]
