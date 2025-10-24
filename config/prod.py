"""
Configuración para PRODUCCIÓN.

Se usa en servidor de producción.
"""
from .default import *

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@prod_host:port/db_name'
