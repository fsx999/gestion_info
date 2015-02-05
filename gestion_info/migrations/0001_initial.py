# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('mac_adresse', macaddress.fields.MACAddressField(max_length=17, null=True)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=10, verbose_name='Num\xe9ro de salle')),
                ('comment', models.TextField(null=True, verbose_name='Commentaire', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeBaseEquipement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=3)),
                ('label', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeEquipement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=32)),
                ('comment', models.TextField(null=True, blank=True)),
                ('base', models.ForeignKey(to='gestion_info.TypeBaseEquipement', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='equipement',
            name='salle',
            field=models.ForeignKey(related_name='equipements', to='gestion_info.Salle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipement',
            name='type',
            field=models.ForeignKey(to='gestion_info.TypeEquipement'),
            preserve_default=True,
        ),
    ]
