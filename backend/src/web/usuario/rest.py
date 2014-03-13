# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb


class Curso(ndb.Model):
    nome = ndb.StringProperty()
    login = ndb.StringProperty()


def salvar(nome, login):
    curso = Curso(nome=nome, login=login)
    curso.put()


def listar(_resp):
    query = Curso.query().order(-Curso.nome)

    def to_dict(c):
        dct = c.to_dict()
        dct['id'] = str(c.key.id())
        return dct

    lista_de_cursos = [to_dict(c) for c in query.fetch()]
    lista_de_cursos = json.dumps(lista_de_cursos)
    _resp.write(lista_de_cursos)