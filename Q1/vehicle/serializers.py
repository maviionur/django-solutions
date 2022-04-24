from rest_framework import serializers
from vehicle.models import NavigationRecord


class NavigationRecordSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.ReadOnlyField(source='vehicle.plate')

    class Meta:
        model = NavigationRecord
        fields = ['latitude', 'longitude', 'vehicle_plate', 'datetime']