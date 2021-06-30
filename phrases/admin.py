from django.contrib import admin

from phrases.models import Verb, Noun


class VerbAdmin(admin.ModelAdmin):
    list_display = ('germanText',
                    'turkishText',
                    'pastTense',
                    'date')
    ordering = ('date',)
    search_fields = ('germanText', 'turkishText', 'pastTense')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class NounAdmin(admin.ModelAdmin):
    list_display = ('germanText',
                    'turkishText',
                    'artikel',
                    'plural',
                    'date')
    ordering = ('date',)
    search_fields = ('germanText', 'turkishText', 'plural')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Verb, VerbAdmin)
admin.site.register(Noun, NounAdmin)