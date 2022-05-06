from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from natives.models import Native
from portfolio.models import Project
from portfolio.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @action(detail=False, methods=['get'])
    def call_someone(self, request):
        return Response({})


class ProjectsForANativeView(APIView):
    def get(self, request, number):
        try:
            native = Native.objects.get(id=number)
            native_projects = Project.objects.filter(native=native)
        except Project.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'No Project Found'})
        if len(native_projects) <= 0:
            return Response({'status': 'error', 'data': "", 'message': 'No Project is registered yet'})
        serializer = ProjectSerializer(native_projects, many=True)
        return Response({'status': 'success', 'data': serializer.data, 'message': 'Projects Found Successfully'})

