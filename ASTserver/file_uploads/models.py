# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FileModel(models.Model):
    testfile = models.FileField(upload_to='documents')