from django.contrib import admin
from posts.models import Post

# Register your models here.

# Decorador
# Se esta mandando al panel de administrador que registre el modelo Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos que se van a desplegar sin tener que acceder al post
    list_display = ['title', 'created_at']
    
# pass