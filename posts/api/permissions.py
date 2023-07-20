# Crear permisos

from rest_framework.permissions import BasePermission

# Si el usuario es de tipo Staff devolvera un True
# Si el usuario no es de tipo Staff no podra accederA
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff