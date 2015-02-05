# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Equipement.ip'
        db.alter_column(u'gestion_info_equipement', 'ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True))

    def backwards(self, orm):

        # Changing field 'Equipement.ip'
        db.alter_column(u'gestion_info_equipement', 'ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

    models = {
        u'gestion_info.equipement': {
            'Meta': {'object_name': 'Equipement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'mac_adresse': ('macaddress.fields.MACAddressField', [], {'max_length': '17', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'salle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion_info.Salle']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion_info.TypeEquipement']"})
        },
        u'gestion_info.salle': {
            'Meta': {'object_name': 'Salle'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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