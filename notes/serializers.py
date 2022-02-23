from rest_framework.serializers import HyperlinkedModelSerializer

from notes.models import Node


class NodeModelSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Node
        fields = '__all__'
