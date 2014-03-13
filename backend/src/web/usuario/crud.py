# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from web.curso.rest import Curso


def index(_write_tmpl):
    query = Curso.query().order(-Curso.nome)
    dct = {'lista_cursos': query.fetch(),
           'um_valor': 10}
    _write_tmpl('/templates/curso_listar.html', dct)


def cadastrar(_write_tmpl, _req):
    path = router.to_path(salvar)
    dct = {'salvar_curso': path, 'req':_req}
    _write_tmpl('/templates/curso_form.html', dct)


def salvar(_handler, nome, login):
    login = login
    curso = Curso(nome=nome, login=login)
    curso.put()
    path = router.to_path(index)
    _handler.redirect(path)
