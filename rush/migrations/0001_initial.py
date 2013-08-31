# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rushie'
        db.create_table(u'rush_rushie', (
            (u'profile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Profile'], unique=True, primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('grad_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'rush', ['Rushie'])


        # Adding SortedM2M table for field majors on 'Rushie'
        db.create_table(u'rush_rushie_majors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rushie', models.ForeignKey(orm[u'rush.rushie'], null=False)),
            ('major', models.ForeignKey(orm[u'main.major'], null=False)),
            ('sort_value', models.IntegerField())
        ))
        db.create_unique(u'rush_rushie_majors', ['rushie_id', 'major_id'])

    def backwards(self, orm):
        # Deleting model 'Rushie'
        db.delete_table(u'rush_rushie')

        # Removing M2M table for field majors on 'Rushie'
        db.delete_table(db.shorten_name(u'rush_rushie_majors'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.major': {
            'Meta': {'object_name': 'Major'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.profile': {
            'Meta': {'object_name': 'Profile'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'rush.rushie': {
            'Meta': {'object_name': 'Rushie', '_ormbases': [u'main.Profile']},
            'grad_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'majors': ('sortedm2m.fields.SortedManyToManyField', [], {'blank': 'True', 'related_name': "'rushies'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['main.Major']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'profile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Profile']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['rush']