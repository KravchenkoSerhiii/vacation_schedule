from rest_framework import viewsets
from .models import Employee, DayOff
from .serializers import EmployeeSerializer, DayOffSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DayOffViewSet(viewsets.ModelViewSet):
    queryset = DayOff.objects.all()
    serializer_class = DayOffSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ["date", "employee"]
    ordering_fields = ["date"]

