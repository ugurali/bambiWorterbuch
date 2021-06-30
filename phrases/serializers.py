from rest_framework import serializers

from phrases.models import Verb, Noun


class VerbCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verb
        fields = ('id', 'germanText', 'turkishText', 'pastTense', 'date')


class VerbSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")

    class Meta:
        model = Verb
        fields = ('id', 'germanText', 'turkishText', 'pastTense', 'date')


class NounCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noun
        fields = ('id', 'germanText', 'turkishText', 'artikel', 'plural', 'date')


class NounSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")

    class Meta:
        model = Noun
        fields = ('id', 'germanText', 'turkishText', 'artikel', 'plural', 'date')