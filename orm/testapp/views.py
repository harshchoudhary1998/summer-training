from django.shortcuts import render
from testapp.models import employee
#from django.db.models.function import Lower
# Create your views here.
def display(request):
    e1=employee.objects.get_emp_range(1000,30000) # ye pana banaya he
    # isme objects customManager ke get_emp_range chalaeyga jisne parent class ke get_queryset chala he jo object.all karta he
    # usme apn kuch modification karke naye implimentation ke sath bhejte he
    dict={'e1':e1}
    return render(request,"testapptemplate/index.html",context=dict)
