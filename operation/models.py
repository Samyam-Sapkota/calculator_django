from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class opr(models.Model):
    int_a=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(-100)],default=0)
    int_b=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(-100)],default=0)
    algebra=models.CharField(max_length=1)
    result=models.IntegerField()

    def __int__(self):
        return self.pk