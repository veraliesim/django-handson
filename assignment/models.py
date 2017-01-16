from __future__ import unicode_literals
from django.db import models
import django.db.models.options as options

class Storedetails(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='Store_name', max_length=1000, blank=True, null=True) 
    store_location = models.CharField(db_column='Store_location', max_length=1000, blank=True, null=True)
    store_hash = models.CharField(db_column='Store_hash', max_length=1000, blank=True, null=True)
    store_description = models.CharField(db_column='Store_description', max_length=1000, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'StoreDetails'

    def __unicode__(self):
        return self.email
