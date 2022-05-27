from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,TakeMessage

# Register your models here.
class CustomAdmin(UserAdmin):
    list_display = ['username','email','is_active','is_staff']
    fieldsets = (
        (None, {
            "fields": (
                'email','username','first_name','last_name','password',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff','is_superuser','is_active',
            ),
        }),
    )

class TakeMeassageAdmin(admin.ModelAdmin):
    list_display = ['email','send_at'] 

admin.site.register(CustomUser,CustomAdmin)    
admin.site.register(TakeMessage,TakeMeassageAdmin)    