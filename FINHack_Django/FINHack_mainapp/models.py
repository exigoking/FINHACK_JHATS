from django.db import models

# Create your models here.

# Nov 19 - for more info https://docs.djangoproject.com/en/1.8/ref/models/fields/

class Mainapp(models.Model):
	email =  models.EmailField()
	name  = models.CharField(max_length = 1000,blank = True, null = True)

	def __unicode__(self):
		return self.email

class CreateRoom(models.Model):
	room_name  = models.CharField(max_length = 1000,blank = True, null = True)

	def __unicode__(self):
		return self.room_name


