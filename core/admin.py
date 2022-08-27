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


class WorkRequest(admin.ModelAdmin):
    list_display=("id","requested_by","work_description","job_date","date_requested","assigned_on","assigned_to","verification")


class ServiceAssignmentAdmin(admin.ModelAdmin):
    list_dislay=("id","date_assigned","worker","service")

admin.site.register(models.ImagesForSlide,ImageAdmin)
admin.site.register(models.MpesaPayment)
admin.site.register(models.UserNotifications,NotificationAdmin)
admin.site.register(models.RequestForService,WorkRequest)
admin.site.register(models.VerificationStatus)
admin.site.register(models.ServiceAssignment,ServiceAssignmentAdmin)
