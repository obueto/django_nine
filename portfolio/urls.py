from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('project', views.ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('project/v1/<int: number>/', views.ProjectsForANativeView.as_view())

]
