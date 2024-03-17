from django.db import models
from django.contrib import admin

# Create your models here.
class Railway(models.Model):
    train_no = models.IntegerField(primary_key=True)
    train_name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_station_code = models.CharField(max_length=10)
    end_station_code = models.CharField(max_length=10)

class RailwayAdmin(admin.ModelAdmin):
    list_display = ('train_no','train_name','start_date','end_date','start_station_code',)
