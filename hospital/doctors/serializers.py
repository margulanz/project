from rest_framework import serializers


from .models import Specialization,Doctor,AppointmentDate,Request



class SpecSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specialization
		fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = AppointmentDate
		fields = "__all__"

class RequestSerializer(serializers.ModelSerializer):
	timeslot = AppointmentSerializer()
	class Meta:
		model = Request
		fields = [
			'timeslot',
			'name',
			'surname',
			'contact_number'
		]
	depth = 1
	def create(self,validated_data):
		timeslot_data = validated_data.pop('timeslot')
		appointment_date = AppointmentDate.objects.create(**timeslot_data)
		request = Request.objects.create(timeslot = appointment_date,**validated_data)
		return request