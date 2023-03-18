from rest_framework import viewsets

from .models import BlogPost
from .serializers import BlogSerializers

# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializers
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)