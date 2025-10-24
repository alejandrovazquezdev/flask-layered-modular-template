"""
Configuración para DESARROLLO COMPARTIDO.

Se usa en servidor de desarrollo compartido entre el equipo.
"""
from .default import *

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@dev_host:port/db_name'
