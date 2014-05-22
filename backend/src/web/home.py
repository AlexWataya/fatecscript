# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import webapp2
from web import my_form
from tekton import router
from web.usuario.rest import Usuario

def index(_write_tmpl):
    _write_tmpl('templates/index.html')