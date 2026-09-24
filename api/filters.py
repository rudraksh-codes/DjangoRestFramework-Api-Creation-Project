import django_filters
from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    min_id = django_filters.CharFilter(method='get_emps_by_empid_range', label='From EMP')
    max_id = django_filters.CharFilter(method='get_emps_by_empid_range', label="To EMP")
    
    class Meta :
        model = Employee
        fields = ['designation', 'emp_name', 'id'] 

    def get_emps_by_empid_range(self, queryset, name, value):
        if name == 'min_id' : 
            return queryset.filter(emp_id__gte=value.upper())
        elif name== 'max_id' : 
            return queryset.filter(emp_id__lte=value.upper())
        return queryset 
