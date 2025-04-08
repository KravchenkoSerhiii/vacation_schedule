from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DayOffViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"dayoffs", DayOffViewSet, basename="dayoff")

urlpatterns = [
    path("", include(router.urls)),
]