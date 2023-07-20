from rest_framework.serializers import ModelSerializer
from posts.models import Post

# Serializers
# sirven para gestionar los datos de nuestros Endpoints

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'order', 'created_at']
        # fields = '__all__' # Mala practica
    
