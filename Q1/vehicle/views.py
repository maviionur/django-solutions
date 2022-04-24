from rest_framework import generics
from vehicle.models import NavigationRecord
from vehicle.serializers import NavigationRecordSerializer


class NavigationRecortList(generics.ListAPIView):
    queryset = NavigationRecord.objects.get_last_records()
    serializer_class = NavigationRecordSerializer