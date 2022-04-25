from rest_framework import serializers
from method1.models import BinOperation


class BinOperationsSerializer(serializers.ModelSerializer):
    operation_name = serializers.ReadOnlyField(source='operation.name')

    class Meta:
        model = BinOperation
        fields = ['bin', 'operation_name', 'collection_frequency']