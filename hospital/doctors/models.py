from django.db import models

categories = [
	('highest','highest'),
	('first','first'),
	('average','average'),
	('low','low')
]
class Doctor(models.Model):
	birth_date = models.DateTimeField()
	IIN = models.CharField(max_length = 12)
	name = models.CharField(max_length = 25)
	surname = models.CharField(max_length = 25)
	middlename = models.CharField(max_length = 25,blank = True)
	contact_number = models.CharField(max_length = 25) # will be added validation in the future
	department_id  = models.IntegerField() # will be foreign key in the future
	specialization_id = models.IntegerField() # will be foreign key in the future
	experience = models.IntegerField()
	photo = models.ImageField(blank = True)
	category = models.CharField(max_length = 25,choices = categories)
	price_for_appointment = models.FloatField()
	schedule_details = models.TextField(max_length = 250)
	education = models.CharField(max_length = 30)
	rating = models.IntegerField()
	address = models.CharField(max_length = 50)
	homepage = models.CharField(max_length = 50,blank = True)

	def __str__(self):
		return f"{self.name} {self.surname}"
	def __repr__(self):
		return f"{self.name} {self.surname}"