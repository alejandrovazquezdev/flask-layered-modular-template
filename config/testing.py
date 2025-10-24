"""
Configuración para TESTING (ejecución de tests).

Se usa cuando se ejecutan las pruebas unitarias.
"""
from .default import *

DEBUG = True
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
