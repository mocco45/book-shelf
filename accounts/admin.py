from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (('credentials', {'fields':('email','password')}),
        ('Personal Info', {'fields':('full_name', 'phone_number', 'profile_photo')}),
        ('Permissions',{'fields':('is_staff', 'is_active')}),
        ('Important Dates', {'fields':('last_login',)})
    )
    
    add_fieldsets = (
        (None, {
         'classes':('wide',),
         'fields': ('email','full_name','phone_number','password1','password2','is_staff','is_active')   
        })
    )
    
    search_fields = ('email',)
    
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
