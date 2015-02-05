# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TypeEquipement'
        db.create_table(u'gestion_info_typeequipement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'gestion_info', ['TypeEquipement'])

        # Adding model 'Salle'
        db.create_table(u'gestion_info_salle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'gestion_info', ['Salle'])

        # Adding model 'Equipement'
        db.create_table(u'gestion_info_equipement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion_info.TypeEquipement'])),
            ('salle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion_info.Salle'])),
            ('mac_adresse', self.gf('macaddress.fields.MACAddressField')(max_length=17, null=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal(u'gestion_info', ['Equipement'])


    def backwards(self, orm):
        # Deleting model 'TypeEquipement'
        db.delete_table(u'gestion_info_typeequipement')

        # Deleting model 'Salle'
        db.delete_table(u'gestion_info_salle')

        # Deleting model 'Equipement'
        db.delete_table(u'gestion_info_equipement')


    models = {
        u'gestion_info.equipement': {
            'Meta': {'object_name': 'Equipement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'mac_adresse': ('macaddress.fields.MACAddressField', [], {'max_length': '17', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'salle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion_info.Salle']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion_info.TypeEquipement']"})
        },
        u'gestion_info.salle': {
            'Meta': {'object_name': 'Salle'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'gestion_info.typeequipement': {
            'Meta': {'object_name': 'TypeEquipement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['gestion_info']