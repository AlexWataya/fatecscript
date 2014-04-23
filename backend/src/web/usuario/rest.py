# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Cardapios(ndb.Model):
    lanche = ndb.StringProperty()
    ingrediente = ndb.StringProperty()
    valor = ndb.StringProperty()

class Usuario(ndb.Model):
    nome = ndb.StringProperty()
    logradouro = ndb.StringProperty()
    num = ndb.StringProperty()
    bairro = ndb.StringProperty()
    cidade = ndb.StringProperty()
    logado = ndb.BooleanProperty()
    admin = ndb.BooleanProperty()

