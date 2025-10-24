"""
Configuración para PREPRODUCCIÓN (Staging).

Se usa en servidor de preproducción, lo más parecido a producción.
Entorno estable para que clientes prueben.
"""
from .default import *

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@staging_host:port/db_name'
