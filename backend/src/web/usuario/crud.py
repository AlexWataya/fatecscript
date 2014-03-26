# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from web.usuario.rest import Usuario



def cadastrar(_write_tmpl, _req):
    _write_tmpl('/templates/cadastro.html')

def como_chegar(_write_tmpl):
    _write_tmpl('/templates/como_chegar.html')

def usuario_listar(_write_tmpl):
    usuarios = Usuario.query().fetch()
    dct = {'lista_usuarios': usuarios}
    _write_tmpl('/templates/usuario_listar.html', dct)

def salvar(_handler, nome, login, password, logradouro, num, bairro, cidade):
    usuario = Usuario(nome=nome, login=login, password=password, logradouro=logradouro, num=num, bairro=bairro, cidade=cidade, logado=True, admin=False)

    usuario.put()

def cardapio(_write_tmpl):
    _write_tmpl('/templates/cardapio.html')

    '''hamburguer = Produto(nome='Hamburguer', descricao='Hamburguer de Piracicaba', preco=11.99)
    rrotDogui = Produto(nome='Hot-Dog', descricao='Hot-Dog de Piracicaba', preco=1.99)
    hamburguer.put()
    rrotDogui.put()
    query = Produto.query()
    dct = {'cardapio': query.fetch()}
    _write_tmpl('/templates/cardapio.html', dct)'''

def foto(_write_tmpl):
    _write_tmpl('/templates/foto.html')
