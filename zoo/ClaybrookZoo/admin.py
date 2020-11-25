from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Animal)
admin.site.register(models.Mammal)
admin.site.register(models.Bird)
admin.site.register(models.Fish)
admin.site.register(models.Reptile)
admin.site.register(models.WatchList)
admin.site.register(models.Sponsor)
admin.site.register(models.Update)
admin.site.register(models.Booking)
admin.site.register(models.AnimalPhoto)
admin.site.register(models.Message)
admin.site.register(models.Feedback)