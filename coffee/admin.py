from django.contrib import admin

from coffee.models import Cafea

@admin.register(Cafea)
class CafeaAdmin(admin.ModelAdmin):
    pass
