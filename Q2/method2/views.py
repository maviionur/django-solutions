from rest_framework import generics
from method2.models import BinOperation
from method2.serializers import BinOperationSerializer

# Create your views here.
class BinOperationList(generics.ListAPIView):
    queryset = BinOperation.objects.select_related().all()
    serializer_class = BinOperationSerializer