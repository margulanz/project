from django.db import models
from django.core.exceptions import ValidationError
categories = [
	('highest','highest'),
	('first','first'),
	('average','average'),
	('low','low')
]



class Specialization(models.Model):
	specialization = models.CharField(max_length = 50,unique=True)
	def __str__(self):
		return f"{self.specialization}"
	def __repr__(self):
		return f"{self.specialization}"


	





class Doctor(models.Model):
	birth_date = models.DateTimeField()
	IIN = models.CharField(max_length = 12)
	name = models.CharField(max_length = 25)
	surname = models.CharField(max_length = 25)
	middlename = models.CharField(max_length = 25,blank = True)
	contact_number = models.CharField(max_length = 25) # will be added validation in the future
	department_id  = models.IntegerField() # will be foreign key in the future
	specialization_id = models.ForeignKey(Specialization,on_delete = models.CASCADE) # will be foreign key in the future
	experience = models.IntegerField()
	photo = models.ImageField(blank = True)
	category = models.CharField(max_length = 25,choices = categories)
	price_for_appointment = models.FloatField()
	schedule_details = models.TextField(max_length = 50)#models.ForeignKey('Schedule',on_delete = models.CASCADE)
	education = models.CharField(max_length = 30)
	rating = models.IntegerField()
	address = models.CharField(max_length = 50)
	homepage = models.CharField(max_length = 50,blank = True)

	def __str__(self):
		return f"{self.name} {self.surname}"
	def __repr__(self):
		return f"{self.name} {self.surname}"
def date_validation(value):
	if not (value.weekday()!=6 and value.weekday()!=5):
		raise ValidationError("This is weekends")
class AppointmentDate(models.Model):
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	date = models.DateField(validators = [date_validation])
	TIMESLOT_LIST = (
        ('09:00 – 09:30', '09:00 – 09:30'),
        ('09:30 – 10:00', '09:30 – 10:00'),
        ('10:00 – 10:30', '10:00 – 10:30'),
        ('10:30 – 11:00', '10:30 – 11:00'),
        ('11:00 – 11:30', '11:00 – 11:30'),
        ('11:30 – 12:00', '11:30 – 12:00'),
        ('12:00 – 12:30', '12:00 – 12:30'),
        ('12:30 – 13:00', '12:30 – 13:00'),
        ('13:00 – 13:30', '13:00 – 13:30'),
        ('13:30 – 14:00', '13:30 – 14:00'),
        ('14:00 – 14:30', '14:00 – 14:30'),
        ('14:30 – 15:00', '14:30 – 15:00'),
        ('15:00 – 15:30', '15:00 – 15:30'),
        ('15:30 – 16:00', '15:30 – 16:00'),
        ('16:00 – 16:30', '16:00 – 16:30'),
        ('16:30 – 17:00', '16:30 – 17:00'),
        ('17:00 – 17:30', '17:00 – 17:30'),)
	timeslot = models.CharField(max_length = 100,choices = TIMESLOT_LIST)
	class Meta:
		unique_together = ('date','timeslot','doctor')
	def __str__(self):
		return f"{self.date} at {self.timeslot} by {self.doctor}"
	def __repr__(self):
		return f"{self.date} at {self.timeslot} by {self.doctor}"
	#schedule = models.ForeignKey(Schedule,on_delete = models.CASCADE)



class Request(models.Model):
	#doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
	timeslot = models.ForeignKey(AppointmentDate,on_delete = models.CASCADE)
	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 30)
	contact_number = models.CharField(max_length = 30)