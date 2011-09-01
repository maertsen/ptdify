# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Area.realm'
        db.add_column('web_area', 'realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Realm'], null=True, blank=True), keep_default=False)

        # Adding field 'Project.realm'
        db.add_column('web_project', 'realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Realm'], null=True, blank=True), keep_default=False)

        # Adding field 'Project.defaultContact'
        db.add_column('web_project', 'defaultContact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Contact'], null=True, blank=True), keep_default=False)

        # Changing field 'Project.area'
        db.alter_column('web_project', 'area_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Area'], null=True))

        # Deleting field 'Contact.area'
        db.delete_column('web_contact', 'area_id')

        # Adding field 'Contact.realm'
        db.add_column('web_contact', 'realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Realm'], null=True, blank=True), keep_default=False)

        # Deleting field 'Context.area'
        db.delete_column('web_context', 'area_id')

        # Adding field 'Context.realm'
        db.add_column('web_context', 'realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Realm'], null=True, blank=True), keep_default=False)

        # Deleting field 'Action.area'
        db.delete_column('web_action', 'area_id')

        # Adding field 'Action.realm'
        db.add_column('web_action', 'realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Realm'], null=True, blank=True), keep_default=False)

        # Adding field 'Action.contact'
        db.add_column('web_action', 'contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Contact'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Area.realm'
        db.delete_column('web_area', 'realm_id')

        # Deleting field 'Project.realm'
        db.delete_column('web_project', 'realm_id')

        # Deleting field 'Project.defaultContact'
        db.delete_column('web_project', 'defaultContact_id')

        # User chose to not deal with backwards NULL issues for 'Project.area'
        raise RuntimeError("Cannot reverse this migration. 'Project.area' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Contact.area'
        raise RuntimeError("Cannot reverse this migration. 'Contact.area' and its values cannot be restored.")

        # Deleting field 'Contact.realm'
        db.delete_column('web_contact', 'realm_id')

        # User chose to not deal with backwards NULL issues for 'Context.area'
        raise RuntimeError("Cannot reverse this migration. 'Context.area' and its values cannot be restored.")

        # Deleting field 'Context.realm'
        db.delete_column('web_context', 'realm_id')

        # User chose to not deal with backwards NULL issues for 'Action.area'
        raise RuntimeError("Cannot reverse this migration. 'Action.area' and its values cannot be restored.")

        # Deleting field 'Action.realm'
        db.delete_column('web_action', 'realm_id')

        # Deleting field 'Action.contact'
        db.delete_column('web_action', 'contact_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web.action': {
            'Meta': {'object_name': 'Action'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Contact']", 'null': 'True', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Context']"}),
            'dependsOn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Action']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Project']", 'null': 'True', 'blank': 'True'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Realm']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'web.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Realm']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'web.contact': {
            'Meta': {'object_name': 'Contact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Realm']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'web.context': {
            'Meta': {'object_name': 'Context'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Realm']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'web.project': {
            'Meta': {'object_name': 'Project'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Area']", 'null': 'True', 'blank': 'True'}),
            'defaultContact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Contact']", 'null': 'True', 'blank': 'True'}),
            'defaultContext': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Context']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Realm']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'web.realm': {
            'Meta': {'object_name': 'Realm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['web']
