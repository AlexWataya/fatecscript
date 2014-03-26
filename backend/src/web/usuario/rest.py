# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nome = ndb.StringProperty()
    login = ndb.StringProperty()
    password = ndb.StringProperty()
    logradouro = ndb.StringProperty()
    num = ndb.StringProperty()
    bairro = ndb.StringProperty()
    cidade = ndb.StringProperty()
    logado = ndb.BooleanProperty()
    admin = ndb.BooleanProperty()

def salvar(nome, login, password, logradouro, num, bairro, cidade):
    usuario = Usuario(nome=nome, login=login, password=password, logradouro=logradouro, num=num, bairro=bairro, cidade=cidade, logado=True, admin=False)
    usuario.put()

def to_dict(c):
    dct = c.to_dict()
    dct['id'] = str(c.key.id())
    return dct

    lista_de_usuarios = [to_dict(c) for c in query.fetch()]
    lista_de_usuarios = json.dumps(lista_de_usuarios)
    _resp.write(lista_de_usuarios)

'''def listar(_resp):
'''