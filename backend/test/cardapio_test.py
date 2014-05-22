
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from base import GAETestCase
from web.cardapio.crud import Cardapios
from mock.mock import Mock
from web.cardapio import crud


class ListarCardapioTest(GAETestCase):
    def test_sucesso(self):
        cardapio = Cardapios(lanche='Teste', ingrediente='Teste', valor='1,99')
        cardapio.put()
        cardapios = [cardapio]
        resposta_mock = Mock()
        crud.cardapio_listar(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/cardapio_listar.html', {'lista_cardapios': cardapios})

class NovoLancheTest(GAETestCase):
    def test_sucesso(self):
        resposta_mock = Mock()
        crud.novo_lanche(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/novo_lanche.html')

class SalvarLancheTest(GAETestCase):
    def test_sucesso(self):
        resposta_mock = Mock()
        lanche = Cardapios(lanche='Teste', ingrediente='Teste', valor='1,99')
        crud.salvar_lanche(resposta_mock, lanche.lanche, lanche.ingrediente, lanche.valor)
        json_str = json.dumps({'id': 1})
        resposta_mock.write.assert_called_once_with(json_str)

class EditarLancheTest(GAETestCase):
    def test_sucesso(self):
        resposta_mock = Mock()
        lanche = Cardapios(lanche='Teste', ingrediente='Teste', valor='1,99')
        lanche.put()
        crud.editar_lanche(resposta_mock, 1, lanche.lanche, lanche.ingrediente, '2,99')
        lanche = Cardapios.get_by_id(1)
        assert lanche.valor == '2,99'

class RemoverLancheTest(GAETestCase):
    def test_sucesso(self):
        resposta_mock = Mock()
        lanche = Cardapios(lanche='Teste', ingrediente='Teste', valor='1,99')
        lanche.put()
        crud.remover_lanche(resposta_mock, 1)
        lanche = Cardapios.get_by_id(1)
        assert not lanche