# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TypeBaseEquipement'
        db.create_table(u'gestion_info_typebaseequipement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'gestion_info', ['TypeBaseEquipement'])

        # Adding field 'TypeEquipement.base'
        db.add_column(u'gestion_info_typeequipement', 'base',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion_info.TypeBaseEquipement'], null=True),
                      keep_default=False)

        # Adding field 'TypeEquipement.comment'
        db.add_column(u'gestion_info_typeequipement', 'comment',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TypeBaseEquipement'
        db.delete_table(u'gestion_info_typebaseequipement')

        # Deleting field 'TypeEquipement.base'
        db.delete_column(u'gestion_info_typeequipement', 'base_id')

        # Deleting field 'TypeEquipement.comment'
        db.delete_column(u'gestion_info_typeequipement', 'comment')


    models = {
        u'gestion_info.equipement': {
            'Meta': {'object_name': 'Equipement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'mac_adresse': ('macaddress.fields.MACAddressField', [], {'max_length': '17', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'salle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipements'", 'to': u"orm['gestion_info.Salle']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion_info.TypeEquipement']"})
        },
        u'gestion_info.salle': {
            'Meta': {'object_name': 'Salle'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'gestion_info.typebaseequipement': {
            'Meta': {'object_name': 'TypeBaseEquipement'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'gestion_info.typeequipement': {
            'Meta': {'object_name': 'TypeEquipement'},
            'base': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion_info.TypeBaseEquipement']", 'null': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['gestion_info']