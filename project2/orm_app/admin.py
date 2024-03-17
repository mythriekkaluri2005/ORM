from django.contrib import admin
from .models import Railway, RailwayAdmin
# Register your models here.
admin.site.register(Railway, RailwayAdmin)