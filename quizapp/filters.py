import django_filters

from .models import Result

class ResultFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='user__first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='user__last_name', lookup_expr='icontains')
    start_total = django_filters.NumberFilter(field_name='total', lookup_expr='gt')
    end_total = django_filters.NumberFilter(field_name='total', lookup_expr='lt')

    class Meta:
        model = Result
        fields = ['first_name', 'last_name', 'start_total', 'end_total']