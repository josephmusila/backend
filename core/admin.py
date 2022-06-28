from django.contrib import admin
from . import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display=("id","first_name","last_name","email","location",)
    ordering = ['first_name']
    search_fields = ['first_name']

admin.site.register(models.User,UserAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display=("id","label","image",)



class NotificationAdmin(admin.ModelAdmin):
    list_display=("id","notification","user","date_created",)
    ordering = ["date_created"]
    autocomplete_fields = ["user"]

admin.site.register(models.ImagesForSlide,ImageAdmin)
admin.site.register(models.MpesaPayment)
admin.site.register(models.UserNotifications,NotificationAdmin)
