from rest_framework.viewsets import ModelViewSet
from organization.models import Project, Subscription
from organization.serializers import ProjectSerializer, SubscriptionSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer