# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from base import GAETestCase
from web.usuario.crud import Usuario
from mock.mock import Mock
from web.usuario import crud

class ComoChegarTest(GAETestCase):
    def test_sucesso(self):
        resposta_mock = Mock()
        crud.como_chegar(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/como_chegar.html')

class UsuarioListarTest(GAETestCase):
    def test_sucesso(self):
        usuario = Usuario(nome='Teste', email='teste@teste.com', google_id='123', admin=False)
        usuario.put()
        usuarios = [usuario]
        resposta_mock = Mock()
        crud.usuario_listar(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/usuario_listar.html', {'lista_usuarios': usuarios})

class FotoTest(GAETestCase):
    def test_sucesso(self):
        resposta_mock = Mock()
        crud.foto(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/foto.html')