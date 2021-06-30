from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from bambi_worterbuch.paginations import MediumResultsSetPagination
from phrases.models import Verb, Noun
from phrases.serializers import VerbCreateSerializer, VerbSerializer, NounCreateSerializer, NounSerializer


class VerbViewSet(viewsets.ModelViewSet):
    queryset = Verb.objects.all()
    pagination_class = MediumResultsSetPagination

    def get_queryset(self):
        return super().get_queryset()\
            .order_by('-date')


    def get_serializer_class(self):
        if self.action == 'create':
            return VerbCreateSerializer
        return VerbSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        term = request.query_params['term']
        verbs = Verb.objects.filter(
            Q(germanText__icontains=term)
            | Q(turkishText__icontains=term)
        )
        page = self.paginate_queryset(verbs)

        serializer = VerbSerializer(
            page, context=verbs, many=True
        )
        return self.get_paginated_response(serializer.data)


class NounViewSet(viewsets.ModelViewSet):
    queryset = Noun.objects.all()
    pagination_class = MediumResultsSetPagination

    def get_queryset(self):
        return super().get_queryset() \
            .order_by('-date')

    def get_serializer_class(self):
        if self.action == 'create':
            return NounCreateSerializer
        return NounSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        term = request.query_params['term']
        nouns = Noun.objects.filter(
            Q(germanText__icontains=term)
            | Q(turkishText__icontains=term)
        )
        page = self.paginate_queryset(nouns)

        serializer = NounSerializer(
            page, context=nouns, many=True
        )
        return self.get_paginated_response(serializer.data)
