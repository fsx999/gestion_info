from __future__ import unicode_literals
# coding=utf-8
from django.contrib import admin
from gestion_info.models import TypeEquipement, Salle, Equipement


class EquipementInline(admin.TabularInline):
    model = Equipement
    extra = 1


class EquipementAdmin(admin.ModelAdmin):
    search_fields = ['salle__label']


class SalleAdmin(admin.ModelAdmin):
    inlines = [EquipementInline]
    search_fields = ['label']


admin.site.register(TypeEquipement)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Salle, SalleAdmin)
