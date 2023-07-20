# Aqui se van a crear las vistas del rest_framework
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer

# IsAuthenticated: Solo los usuarios loggeados pueden acceder a los datos de la clase
# IsAdminUser: Solo los usuarios administradores podran acceder a los datos de el modelo
# IsAuthenticatedOrReadOnly: Solo los usuarios autenticados podran hacer algo(CRUD), los demas solo podran leer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly


""" 
APIView tiene el metodo GET, POST, PUT, DELETE
"""

# CREATE READ DELETE UPDATE con ModelViewSet
class PostModelViewSet(ModelViewSet):
    # Añadiendo permisos a una clase
    permission_classes = [IsAdminOrReadOnly] # Se puede añadir mas de un permiso
    
    # CRUD completo
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # http_method_names = ['get', 'put'] # Para especificar metodos que se vayan a utilizar


""" 
class PostViewSet(ViewSet):
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def create(self, request):
        serializer = PostSerializer(data=request.POST)
        # Si no es valido entonces lanzara una excepcion
        serializer.is_valid(raise_exception = True)
        # Para guardar el dato en la base de datos 
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    # Endpoint que solo devolvera un post
    def retrieve(self, request, pk:int):
        # El pk sera el id de el elemento que se mostrara en la url
        # Para obetener un solo elemento de la tabla Post
        # Para obtener el post mediante el pk (numero id)
        post = PostSerializer(Post.objects.get(pk=pk))
        
        # Para obtener el post mediante su nombre
        # post = PostSerializer(Post.objects.get(title=title))
        
        return Response(status=status.HTTP_200_OK, data=post.data)
    
 """

""" 
class PostApiView(APIView):
    def get(self, request):
        # Se le dice al ORM Django que del modelo Post tenga todos los elementos de la base de datos
        # y los guarde en la variable posts
        # posts = Post.objects.all()
        # posts = [post.title for post in Post.objects.all()]
        # return Response(status=status.HTTP_200_OK, data=posts)
        
        # Serializador
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        # return Response(status=status.HTTP_200_OK, data='Hola mundo')
    
    # Endpoint para crear nuevos posts
    # def post(self, request):
    #     Post.objects.create(
    #         title = request.POST['title'],
    #         description = request.POST['description'],
    #         order = request.POST['order'])
        
    #     return self.get(request)
    def post(self, request):
        serializer = PostSerializer(data=request.POST)
        # Si no es valido entonces lanzara una excepcion
        serializer.is_valid(raise_exception = True)
        # Para guardar el dato en la base de datos 
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
     """
