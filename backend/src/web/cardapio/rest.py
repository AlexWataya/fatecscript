# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Cardapios(ndb.Model):
    lanche = ndb.StringProperty()
    ingrediente = ndb.StringProperty()
    valor = ndb.StringProperty()

