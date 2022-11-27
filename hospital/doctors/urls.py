from django.urls import path
from .views import SpecView,DoctorView,TimeSlotView,RequestView


urlpatterns = [
	path("specializations/",SpecView.as_view({"get":"list",'post':'create'}), name = "specs"),
	path('specializations/<int:id>/doctors/',DoctorView.as_view({'get':'list'})),
	path('doctors/',DoctorView.as_view({'get':'list'})),
	path('time-slots/<int:id>/',TimeSlotView.as_view({'get':'list'})),
	path('time-slots/',TimeSlotView.as_view({'get':'list','post':'create'})),
	path('requests/',RequestView.as_view({'get':'list','post':'create'}))


]