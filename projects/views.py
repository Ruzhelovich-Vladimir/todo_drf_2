from rest_framework.viewsets import ModelViewSet
from .models import Project, Development
from .serializers import ProjectModelSerializer, DevelopmentModelSerializer


class ProjectModelViewSet(ModelViewSet):

    queryset = Project.objects.all()

    serializer_class = ProjectModelSerializer


class DevelopmentModelViewSet(ModelViewSet):

    queryset = Development.objects.all()

    serializer_class = DevelopmentModelSerializer