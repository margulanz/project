from django.contrib import admin
from .models import Doctor,Specialization,AppointmentDate,Request#,Schedule,Request
# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
	list_display = ['name','middlename','surname','category','rating','price_for_appointment']


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Specialization)
admin.site.register(AppointmentDate)
#admin.site.register(Schedule)
admin.site.register(Request)