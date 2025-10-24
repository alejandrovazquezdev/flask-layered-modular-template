from flask_testing import TestCase
from app import create_app, db

class BaseTestClass(TestCase):
    def create_app(self):
        """
        Define la configuración de la aplicación para el entorno de testing
        y retorna la aplicación
        """
        app = create_app('testing')
        return app
    
    def setUp(self):
        """
        Se ejecuta antes de cada test.
        Crea las tablas de la base de datos y la puebla con datos de prueba
        """
        db.create_all()
        self.populate_db()
        
    def tearDown(self):
        """
        Se ejecuta después de cada test.
        Elimina la sesión actual y todas las tablas de la base de datos
        """
        db.session.remove()
        db.drop_all()
        
    def populate_db(self):
        """
        Puebla la base de datos con datos de prueba
        """
        # TODO: Agregar datos de prueba aquí
        pass