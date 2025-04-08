from rest_framework import serializers
from .models import Employee, DayOff


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DayOffSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source="employee")

    class Meta:
        model = DayOff
        fields = ["id", "date", "employee", "employee_id"]
