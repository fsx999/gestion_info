# coding=utf-8
from __future__ import unicode_literals
from django.db import  models
from macaddress.fields import MACAddressField


class TypeEquipement(models.Model):
    label = models.CharField(max_length=32)


class Salle(models.Model):
    """ Salle de l'institut
    """
    label = models.CharField(max_length=10, verbose_name='Numéro de salle')
    comment = models.TextField(null=True, verbose_name="Commentaire")


class Equipement(models.Model):
    name = models.CharField(max_length=32)
    type = models.ForeignKey(TypeEquipement)
    salle = models.ForeignKey(Salle)
    mac_adresse = MACAddressField(integer=False, null=True)
    ip = models.IPAddressField(null=True, blank=True)
