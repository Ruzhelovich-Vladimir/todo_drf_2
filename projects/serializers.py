from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, Development


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Project
        fields = '__all__'

class DevelopmentModelSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Development
        fields = '__all__'
