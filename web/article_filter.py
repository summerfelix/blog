from rest_framework import filters
import django_filters

from backweb.models import Article


class ArticleFilter(filters.FilterSet):

    title = django_filters.CharFilter('title', lookup_expr='contains')
    tags = django_filters.CharFilter('tags', lookup_expr='contains')
    column_id = django_filters.NumberFilter('column_id', lookup_expr='exact')

    class Meta:
        model = Article
        fields = ['title', 'column_id', 'tags']

