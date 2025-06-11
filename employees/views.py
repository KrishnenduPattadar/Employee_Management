from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee, Department
from .serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    EmployeeProfileSerializer
)
from .permissions import IsHRManager, IsEmployeeAndSelf

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['department', 'role', 'employment_status']

    def get_permissions(self):
        user = self.request.user
        if user.is_authenticated and getattr(user, 'is_hr_manager', False):
            return [IsAuthenticated()]
        return [IsEmployeeAndSelf()]

    def get_serializer_class(self):
        user = self.request.user
        if user.is_authenticated and getattr(user, 'is_hr_manager', False):
            return EmployeeSerializer
        return EmployeeProfileSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsHRManager]
