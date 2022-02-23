from rest_framework.viewsets import ModelViewSet

from notes.models import Node
from notes.serializers import NodeModelSerializer


class NodeModelViewSet(ModelViewSet):

    queryset = Node.objects.all()

    serializer_class = NodeModelSerializer

