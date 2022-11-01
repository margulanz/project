from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
	list_display = ['name','middlename','surname','blood_group','contact_number','marital_status']

admin.site.register(Patient,PatientAdmin)