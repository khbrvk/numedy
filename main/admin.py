from django.contrib import admin
from .models import Storage, Employee, Item, Supply, Manufaturer

admin.site.register(Storage)
admin.site.register(Employee)
admin.site.register(Item)
admin.site.register(Supply)
admin.site.register(Manufaturer)