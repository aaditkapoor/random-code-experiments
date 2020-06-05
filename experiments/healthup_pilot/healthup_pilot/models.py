from django.db import models


class UserModel(models.Model):
	name = models.CharField(max_length=32)
	email = models.CharField(max_length=200)
	sex = models.CharField(max_length=20)
	age = models.CharField(max_length=30)
	number = models.CharField(max_length=11)
	weight = models.CharField(max_length=3)
	height = models.CharField(max_length=3)
	fitness_goal = models.CharField(max_length=100)
	activeness = models.CharField(max_length=60)



	def __str__(self):
		return self.name + "with" + self.email




