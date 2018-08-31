# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class classname(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    section = models.CharField(max_length=2)

    def __str__(self):
        return str(self.name)+'='+str(self.rollno)+'='+str(self.section)