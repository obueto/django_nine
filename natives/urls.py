from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('natives', views.NativeViewSet, basename='natives')
router.register('cohort', views.CohortViewSet, basename='cohort')

urlpatterns = [
    path('', include(router.urls)),
    path('natives/v1/<int: number>/', views.NativesInCohortView.as_view())

]
