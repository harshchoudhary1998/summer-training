import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'orm.settings')

import django
django.setup() # django ke seeting change karne me kamm atta he

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()

def populate(n):
    for i in range(n):
        fname=fake.name()
        fcity=fake.city()
        fno=randint(1000,5000)
        fsal=randint(10000,50000)
        employee.objects.get_or_create(name=fno,ename=fname,ecity=fcity,esal=fsal)

populate(25)
