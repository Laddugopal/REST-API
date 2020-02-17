from django.contrib import admin
from laddu_rest_api import models 

#below command registers the user profile model as a admin site register
admin.site.register(models.UserProfile)

# Register your models here.
