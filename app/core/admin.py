from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name')
    list_filter = ('name',)
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }), #DO NOT FORGET ,(COMMA) HERE, BECAUSE IN THIS TUPLE ONLY ONE ELEMENT!
    )
    
    

admin.site.register(models.User, UserAdmin)
