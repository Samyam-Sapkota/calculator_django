from django.contrib import admin
from .models import opr
# Register your models here.

class front_db_view(admin.ModelAdmin):
    list_display=('int_a','int_b','algebra','result')


admin.site.register(opr,front_db_view)