# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import webapp2
from web import my_form
from tekton import router
from web.usuario.rest import Usuario

def login(_write_tmpl):
     _write_tmpl('/templates/login.html')

def efetuar_login(_write_tmpl, _handler, nome, senha):
    usuario = Usuario.query(Usuario.nome == nome, Usuario.password == senha).fetch()
    if usuario:
        setattr(usuario[0], 'logado', True)
        usuario[0].put()
        _handler.redirect('/')
    else:
        _write_tmpl('/templates/login.html')


def index(_write_tmpl):
    url = router.to_path(my_form)
    usuario = Usuario.query(Usuario.logado==True).fetch()
    dict = {}
    if usuario:
        dict = {'form_url': url,
                'is_admin': usuario[0].admin,
                'is_logged': True
            }
    else:
        dict = {'form_url': url,
                'is_admin': False,
                'is_logged': False
            }

    _write_tmpl('templates/index.html', dict)


def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)

