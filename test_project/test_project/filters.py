from django_filters import FilterSet
from django_filters import CharFilter

class TestFilter(FilterSet):
  test_filter = CharFilter(
    field_name='global_company__baaz_registration_code', lookup_expr='icontains')

  class Meta:
    # model = CompanyUsers
    fields = ['test_filter']