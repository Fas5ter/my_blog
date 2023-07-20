"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import HelloWorld
# from posts.api.views import PostApiView
# from posts.api.views import PostViewSet
from posts.api.router import router_post
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from posts.api.router import router_post

schema_view = get_schema_view(
   openapi.Info(
      title="DOCUMENTACION API BLOG",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # EndPoint
    # path('api/posts/', PostApiView.as_view())
    
    # ViewSet
    path('api/', include(router_post.urls)),
    
    # Home
    # path('', HelloWorld.as_view())
    
    path("api/", include('user.api.router')),
    
    # drf-yasg (Documentacion)
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]