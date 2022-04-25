from rest_framework import generics
from method1.models import BinOperation
from method1.serializers import BinOperationsSerializer

# Create your views here.
class BinOperationList(generics.ListAPIView):
    queryset = BinOperation.objects.select_related().all()
    serializer_class = BinOperationsSerializer