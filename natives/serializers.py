from rest_framework import serializers
from .models import Native, Cohort


# what ever data you want to sen should be a list, dictionary or serializer
class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = "__all__"


class NativeSerializer(serializers.ModelSerializer):
    # cohort = serializers.SerializerMethodField()
    # mumu = serializers.SerializerMethodField()

    class Meta:
        model = Native
        fields = "__all__"
    #  @staticmethod
    # def get_cohort(self, obj):
    #  return obj.cohort.name

# def get_mumu(self, obj):
#    return "Not Fola"
