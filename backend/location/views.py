from rest_framework import generics
from .models import Zipcode
from .serializers import ZipcodeSerializer
# Search and Filter zipcode packages:
from rest_framework import filters
from .filters import DynamicSearchFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ZipcodeList(generics.ListAPIView):
    queryset = Zipcode.objects.all()
    serializer_class = ZipcodeSerializer
    filter_backends = [DynamicSearchFilter, DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['zipcode']
    # filter_backends = [filters.SearchFilter]
    search_fields = ['zipcode']

class ZipcodeDetail(generics.RetrieveAPIView):
    queryset = Zipcode.objects.all()
    serializer_class = ZipcodeSerializer   