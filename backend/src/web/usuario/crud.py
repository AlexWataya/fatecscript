# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from web.usuario.rest import Usuario

def como_chegar(_write_tmpl):
    _write_tmpl('/templates/como_chegar.html')

def usuario_listar(_write_tmpl):
    usuarios = Usuario.query().fetch()
    dct = {'lista_usuarios': usuarios}
    _write_tmpl('/templates/usuario_listar.html', dct)

def foto(_write_tmpl):
    _write_tmpl('/templates/foto.html')