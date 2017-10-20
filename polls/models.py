from django.db import models

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	std=models.CharField(max_length=10)
	title=models.CharField(max_length=50)
	text = models.TextField()
	
	def __str__(self):
		return self.title

