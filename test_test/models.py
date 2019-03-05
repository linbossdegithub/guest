# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Event(models.Model):
	name = models.CharField(max_length=100)
	limit = models.IntegerField()
	status = models.BooleanField()
	address =models.CharField(max_length=200)
	start_time = models.DateTimeField('events time')
	create_time = models.DateTimeField(auto_now=True)
	def ___str___(self):
		return self.name


class Guest(models.Model):
	event = models.ForeignKey(Event)
	realname = models.CharField(max_length=64)
	phone = models.CharField(max_length=16)
	email = models.EmailField()
	sign = models.BooleanField() 
create_time = models.DateTimeField(auto_now=True)

class Meta:
	unique_together = ("event","phone")

def ___str___(self):
	return self.realname
