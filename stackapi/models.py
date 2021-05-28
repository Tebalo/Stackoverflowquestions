from django.db import models

# Create your models here.
class Question(models.Model):
	question = models.CharField(max_length=300)
	vote_count = models.IntegerField(default=0)
	views = models.CharField(max_length=50)
	tags = models.CharField(max_length=250)

	def __str__(self):
		return self.question

class User(models.Model): # Edit 6
	userId = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50,blank=False, verbose_name="name")
	phone = models.CharField(max_length=20,blank=False, verbose_name="Phone number")
	email = models.EmailField(max_length=50,blank=False, verbose_name="Email")

	def __str__(self):
		return self.name 