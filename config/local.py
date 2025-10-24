"""
Configuración para DESARROLLO LOCAL.

Se usa en el entorno local de cada desarrollador.
Hereda de default.py y especifica SQLALCHEMY_DATABASE_URI local.
"""
from .default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///miniblog.db'
