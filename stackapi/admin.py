from django.contrib import admin
from stackapi import models# Edit 7
# Register your models here.
from .models import Question

admin.site.register(Question)
admin.site.register(models.User)# Edit 6
