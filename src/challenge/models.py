from django.db import models

# Create your models here.

# Create a model to store uploaded file (dictionary of words, via .txt file)
class Dictionary(models.Model):
	# Set file title, use CharField
	title		= models.CharField(max_length=50)
	# Set file descirption, use TextField
	description = models.TextField()
	# Set file upload path to 'Media_Root', use FileField
	file 		= models.FileField(upload_to = 'dictionary/%Y/%m/%d')