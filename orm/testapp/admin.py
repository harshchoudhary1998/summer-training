from django.contrib import admin
from testapp.models import employee
# Register your models here.
class adminemployee(admin.ModelAdmin):
    list_display=['name','ename','esal','ecity']

admin.site.register(employee,adminemployee)
