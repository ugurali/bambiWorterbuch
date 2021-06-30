from django_filters import rest_framework as filters

from phrases.models import Verb, Noun


class NounFilter(filters.FilterSet):
    germanText = filters.CharFilter(field_name='germanText', lookup_expr='icontains')
    turkishText = filters.CharFilter(field_name='turkishText', lookup_expr='icontains')
    plural = filters.CharFilter(field_name='plural', lookup_expr='icontains')

    class Meta:
        model = Noun
        exclude = ['artikel', 'date']


class VerbFilter(filters.FilterSet):
    germanText = filters.CharFilter(field_name='germanText', lookup_expr='icontains')
    turkishText = filters.CharFilter(field_name='turkishText', lookup_expr='icontains')
    pastTense = filters.CharFilter(field_name='pastTense', lookup_expr='icontains')

    class Meta:
        model = Verb
        exclude = ['date']