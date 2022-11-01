from django.db import models


blood_groups = [
	('O-','O-'),
	('O+','O+'),
	('A-','A-'),
	('A+','A+'),
	('B-','B-'),
	('B+','B+'),
	('AB-','AB-'),
	('AB+','AB+'),
]

marital_statuses = [
	('single', 'single'),
	('married','married'), 
	('widowed','widowed'), 
	('divorced','divorced'), 
	('separated','separated')
]
# Create your models here.
class Patient(models.Model):
	birth_date = models.DateTimeField()
	IIN = models.CharField(max_length = 12)
	name = models.CharField(max_length = 25)
	surname = models.CharField(max_length = 25)
	middlename = models.CharField(max_length = 25,blank = True)
	blood_group = models.CharField(max_length = 10, choices = blood_groups)
	emergency_contact_number = models.CharField(max_length = 25) # will be added validation in the future
	contact_number = models.CharField(max_length = 25) # will be added validation in the future
	email = models.CharField(max_length = 25,blank = True) # will be added validation in the future
	address = models.CharField(max_length = 50)
	marital_status = models.CharField(max_length = 50,choices = marital_statuses)
	registration_date = models.DateTimeField(auto_now_add=True)
	