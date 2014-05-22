# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from tekton import router
from web.cardapio.rest import Cardapios

def cardapio_listar(_write_tmpl):
    cardapios = Cardapios.query().fetch()
    dct = {'lista_cardapios': cardapios}
    _write_tmpl('/templates/cardapio_listar.html', dct)

def listar(_resp):
    query = Cardapios.query().order(-Cardapios.lanche, -Cardapios.ingrediente, -Cardapios.valor, -Cardapios.key)

    def to_dict(c):
        dct = c.to_dict()
        dct['id'] = str(c.key.id())
        return dct

    lista_cardapios = [to_dict(c) for c in query.fetch()]
    lista_cardapios = json.dumps(lista_cardapios)
    _resp.write(lista_cardapios)

def salvar_lanche(_resp, lanche, ingrediente, valor):
    cardapio = Cardapios(lanche=lanche, ingrediente=ingrediente, valor=valor)
    key = cardapio.put()
    json_str = json.dumps({'id': key.id()})
    _resp.write(json_str)

def editar_lanche(_resp, idCardapio, lanche, ingrediente, valor):
    cardapio = Cardapios.get_by_id(int(idCardapio))
    cardapio.lanche = lanche
    cardapio.ingrediente = ingrediente
    cardapio.valor = valor
    cardapio.put()

def remover_lanche(_resp, idCardapio):
    cardapio = Cardapios.get_by_id(int(idCardapio))
    cardapio.key.delete()

def novo_lanche(_write_tmpl):
   _write_tmpl('/templates/novo_lanche.html')