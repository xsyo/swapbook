from django.contrib import admin

from .models import Sentence


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('who_offers', 'whomever_is_offered')
