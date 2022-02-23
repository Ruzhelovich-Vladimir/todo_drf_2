from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):

    queryset = Author.objects.all()

    serializer_class = AuthorModelSerializer