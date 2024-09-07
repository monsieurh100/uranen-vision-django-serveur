import django_filters
from .models import Article, stock_autre

class ArticleFilter(django_filters.FilterSet):
    site = django_filters.NumberFilter(field_name='stock_autre__site', lookup_expr='exact')
    type_operation = django_filters.NumberFilter(field_name='stock_autre__type_operation', lookup_expr='exact')

    class Meta:
        model = Article
        fields = ['site', 'type_operation']
