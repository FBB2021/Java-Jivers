from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext,gettext_lazy as _
from .models import User
# Register your models here.

class NewUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name' )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'role')}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )

    list_display = ('UserId', 'username', 'role', 'email', 'is_active', 'last_login')
    list_display_links = ('UserId', 'username', 'role', 'email', 'last_login')
    search_fields = ('username', 'email')

admin.site.register(User, NewUserAdmin)