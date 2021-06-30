from django.db import models


class Noun(models.Model):
    germanText = models.CharField(max_length=50, blank=False, null=False)
    turkishText = models.CharField(max_length=50, blank=False, null=False)
    artikel = models.CharField(max_length=5, blank=False, null=False)
    plural = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)


class Verb(models.Model):
    germanText = models.CharField(max_length=100, blank=False, null=False)
    turkishText = models.CharField(max_length=100, blank=False, null=False)
    pastTense = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)