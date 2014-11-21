# coding=utf-8
from __future__ import unicode_literals
from django.db import  models
from django.utils.encoding import python_2_unicode_compatible
from macaddress.fields import MACAddressField


@python_2_unicode_compatible
class TypeEquipement(models.Model):
    label = models.CharField(max_length=32)

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Salle(models.Model):
    """ Salle de l'institut
    """
    label = models.CharField(max_length=10, verbose_name='Numéro de salle')
    comment = models.TextField(null=True, verbose_name="Commentaire", blank=True)

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Equipement(models.Model):
    name = models.CharField(max_length=32)
    type = models.ForeignKey(TypeEquipement)
    salle = models.ForeignKey(Salle)
    mac_adresse = MACAddressField(integer=False, null=True)
    ip = models.IPAddressField(null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.salle.label, self.type, self.name)
