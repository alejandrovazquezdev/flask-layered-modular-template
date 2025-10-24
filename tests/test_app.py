import unittest
from app import create_app, db
from app.auth.models import User


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(settings_module="config.testing")
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()
            # Crea un usuario administrador
            admin = User(name="admin", email="admin@test.com", is_admin=True)
            admin.set_password("admin")
            admin.save()
            # Crea un usuario invitado
            guest = User(name="guest", email="guest@test.com")
            guest.set_password("guest")
            guest.save()

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.remove()
            db.drop_all()
            
    def login(self, email, password):
        """Helper para simular el login de un usuario"""
        with self.app.app_context():
            user = User.get_by_email(email)
            if user and user.check_password(password):
                return user
            return None