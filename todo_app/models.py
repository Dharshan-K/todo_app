from django.db import models

# Create your models here.


class Tasks(models.Model):
	status_choices=[("Pending","Pending"),("Finished","Finished")]
	Title = models.CharField(max_length=250)
	description = models.CharField(max_length=1000)
	status = models.CharField(max_length=20,choices=status_choices,default="pending")
