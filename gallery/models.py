# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Gallery(models.Model):
    description = models.CharField(max_length=100)
