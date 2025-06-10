from rest_framework import viewsets, filters
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer, EmployeeProfileSerializer
from .permissions import IsHRManager, IsEmployeeAndSelf
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['department', 'role', 'employment_status']

    def get_permissions(self):
        if self.request.user.is_hr_manager:
            return [IsAuthenticated()]
        return [IsEmployeeAndSelf()]

    def get_serializer_class(self):
        if self.request.user.is_hr_manager:
            return EmployeeSerializer
        return EmployeeProfileSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsHRManager]
