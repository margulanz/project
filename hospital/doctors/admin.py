from django.contrib import admin
from .models import Doctor
# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
	list_display = ['name','middlename','surname','category','rating','price_for_appointment']


admin.site.register(Doctor,DoctorAdmin)