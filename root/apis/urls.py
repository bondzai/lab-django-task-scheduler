from django.urls import path, include
from rest_framework import routers
from apis.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
