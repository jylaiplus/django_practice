#from __future__ import unicode_literals
from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name

class Show(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_3D = models.BooleanField()
    cinema = models.ForeignKey(Cinema)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['price']


class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    date_time = models.DateTimeField()
    cinema = models.ForeignKey(Cinema)