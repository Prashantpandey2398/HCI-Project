from django.contrib import admin

# Register your models here.
from sis.models import UserProfile,Marksheets

class UserAdmin(admin.ModelAdmin):
    pass

class MarksAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Marksheets, MarksAdmin)
