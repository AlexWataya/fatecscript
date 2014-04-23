# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from web.usuario.rest import Usuario
from web.usuario.rest import Cardapios



def cadastrar(_write_tmpl, _req):
    path = router.to_path(salvar)
    dct = {'salvar': path, 'req': _req}
    _write_tmpl('/templates/cadastro.html')

def como_chegar(_write_tmpl):
    _write_tmpl('/templates/como_chegar.html')

def usuario_listar(_write_tmpl):
    usuarios = Usuario.query().fetch()
    dct = {'lista_usuarios': usuarios}
    _write_tmpl('/templates/usuario_listar.html', dct)

def salvar(_handler, nome, logradouro, num, bairro, cidade):
    usuario = Usuario(nome=nome, logradouro=logradouro, num=num, bairro=bairro, cidade=cidade)
    usuario.put()

def cardapio_listar(_write_tmpl):
    cardapios = Cardapios.query().fetch()
    dct = {'lista_cardapios': cardapios}
    _write_tmpl('/templates/cardapio_listar.html', dct)

def salvarCardapio(_handler, lanche, ingrediente, valor):
    cardapios = Cardapios(lanche=lanche, ingrediente=ingrediente, valor=valor)
    cardapios.put()

def cardapios(_write_tmpl):
    _write_tmpl('/templates/cardapios.html')

def cardapio(_write_tmpl):
    _write_tmpl('/templates/cardapio.html')

def foto(_write_tmpl):
    _write_tmpl('/templates/foto.html')
