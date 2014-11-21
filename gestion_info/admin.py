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
    search_fields = ['label', 'equipements__mac_adresse']
    list_display = ['__str__', 'liste_equipement']
    readonly_fields = ['liste_equipement']

    def liste_equipement(self, obj):
        result = ''
        for equipement in obj.equipements.all():
            result += str(equipement) + '<br>'
        return result
    liste_equipement.allow_tags = True


admin.site.register(TypeEquipement)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Salle, SalleAdmin)
