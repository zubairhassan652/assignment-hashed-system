from rest_framework.routers import DefaultRouter
from organization.views import ProjectViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("subscriptions", SubscriptionViewSet, basename="subscriptions")

urlpatterns = router.urls