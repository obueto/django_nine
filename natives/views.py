# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from natives.models import Cohort, Native
from natives.serializers import CohortSerializer, NativeSerializer


class NativeViewSet(viewsets.ModelViewSet):
    serializer_class = NativeSerializer
    queryset = Native.objects.all()

    @action(detail=False, methods=['get'])
    def call_fola(self, request):
        return Response({})


class NativesInCohortView(APIView):
    def get(self, request, number):
        try:
            cohort = Cohort.objects.get(id=number)
            cohort_natives = Native.objects.filter(cohort=cohort)
        except Native.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'No Native Found'})
        if len(cohort_natives) <= 0:
            return Response({'status': 'error', 'data': "", 'message': 'No Native is registered yet'})
        serializer = NativeSerializer(cohort_natives, many=True)
        return Response({'status': 'error', 'data': serializer.data, 'message': 'Natives found successfully'})


class CohortViewSet(viewsets.ModelViewSet):
    serializer_class = CohortSerializer
    queryset = Cohort.objects.all()

    @action(detail=False, methods=['get'])
    def get_cohort_by_name(self, request):
        cohort_name = self.request.query_params.get('cohort_name')
        cohort = Cohort.objects.get(name=cohort_name)
        serializers = CohortSerializer(cohort)
        return Response(serializers.data)
