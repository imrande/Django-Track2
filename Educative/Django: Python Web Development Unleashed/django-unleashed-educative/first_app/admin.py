from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = ('topic_name',)

@admin.register(models.Webpage)
class WebpageAdmin(admin.ModelAdmin):
	list_display = ('topic', 'name')

@admin.register(models.AccessRecord)
class AccessRecordAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_field')