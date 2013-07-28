# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):


    def forwards(self, orm):
        # Adding field 'Brother_majors.sort_value'
        db.add_column(u'main_brother_majors', 'sort_value',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Brother_majors.sort_value'
        db.delete_column(u'main_brother_majors', 'sort_value')