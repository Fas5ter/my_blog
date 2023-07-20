from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        # titulo, {campos: (campo1, campo2, campoN)}
        (None, {'fields': ('username', 'password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Redes Sociales', {'fields': ('web_site', 'twitter', 'facebook',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )
    # pass