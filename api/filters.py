import django_filters
from Home.models import WatchList

class WatchListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )
    platform = django_filters.CharFilter(
        field_name='platform',
        lookup_expr='exact'
    )
    class Meta:
        model=WatchList
        fields=['title','platform']