from django.db import models

# Create your models here.
class customManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('esal')
    def get_emp_range(self,range1,range2):
        return super().get_queryset().filter(esal__range=(range1,range2)).order_by('esal')


class employee(models.Model):
    name=models.CharField(max_length=30)
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    ecity=models.CharField(max_length=30)
    objects=customManager()  #jaise apn object.all karenge ye banda customManager ka get_queryset chalaeyga
    # wo parent class ka chalaeyga or uss par order_by karke likhega
    # agar apn specify nahi karenge to manager class get_queryset chalta he automatically
    # but apn ne uski implemenatation change kar de
