from django.contrib import admin

# Register your models here.
from .models import Address, Person #, Photo

admin.site.register(Address)
admin.site.register(Person)
# admin.site.register(Photo)
