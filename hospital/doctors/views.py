from rest_framework import viewsets
from .models import Specialization,Doctor,AppointmentDate,Request
from .serializers import SpecSerializer, DoctorSerializer,AppointmentSerializer,RequestSerializer




class SpecView(viewsets.ModelViewSet):
	queryset = Specialization.objects.all()
	serializer_class = SpecSerializer



class DoctorView(viewsets.ModelViewSet):
	#queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	def get_queryset(self):
		if self.kwargs.get('id'):
			queryset = Doctor.objects.filter(specialization_id = self.kwargs.get('id'))
		else:
			queryset = Doctor.objects.all()
		return queryset

class TimeSlotView(viewsets.ModelViewSet):
	#queryset = AppointmentSerializer.objects.all()
	serializer_class = AppointmentSerializer
	def get_queryset(self):
		if self.kwargs.get('id'):
			queryset = AppointmentDate.objects.filter(doctor = self.kwargs.get('id'))
		else:
			queryset = AppointmentDate.objects.all()
		return queryset

class RequestView(viewsets.ModelViewSet):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer