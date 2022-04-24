from dataclasses import field
from gc import collect
from pyexpat import model
from rest_framework import serializers
from method2.models import BinOperation


class BinOperationSerializer(serializers.ModelSerializer):
    operation_name = serializers.ReadOnlyField(source='operation.name')
    collection_frequency = serializers.ReadOnlyField(
                                source='attributes.collection_frequency')

    class Meta:
        model = BinOperation
        fields = ['bin', 'operation_name', 'collection_frequency']