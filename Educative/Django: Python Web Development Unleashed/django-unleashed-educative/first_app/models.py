from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	topic_name = models.CharField(max_length=250, unique=True)

	def __str__(self):
		return self.topic_name

class Webpage(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
	date_field = models.DateField(default=date.today) 
	count = models.IntegerField(default=0)

	def __str__(self):
		return str(self.date_field)

class Post(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to='upload_location', 
            null=True, 
            blank=True, 
            )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title