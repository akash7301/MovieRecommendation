from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Movie(models.Model):
	title   	= models.CharField(max_length=200)
	genres 		= models.CharField(max_length=100)
	movie_url  = models.URLField()

	def __str__(self):
		return self.title

class Myrating(models.Model):
	user   	= models.ForeignKey(User,on_delete=models.CASCADE)
	movie 	= models.ForeignKey(Movie,on_delete=models.CASCADE)
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])

class MovieBulkUpload(models.Model):
	data_upload = models.DateTimeField(auto_now=True)
	csv_file = models.FileField(upload_to='Movie/bulkupload')
