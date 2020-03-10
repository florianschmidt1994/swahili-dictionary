from django.contrib import admin

# Register your models here.
from .models import English
from .models import Swahili


class EnglishAdmin(admin.ModelAdmin):
    list_display = ("english_word", "swahili_word")


class SwahiliAdmin(admin.ModelAdmin):
    list_display = ("swahili_word", "english_word")


admin.site.register(English, EnglishAdmin)
admin.site.register(Swahili, SwahiliAdmin)
