import unittest

from tests.test_app import BaseTestClass
from app import db
from app.auth.models import User
from app.models import Post


class BlogClientTestCase(BaseTestClass):

    def test_index_with_no_posts(self):
        """Verifica que se muestra el mensaje de advertencia cuando no hay posts"""
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        # como no hay posts, no hay nada que verificar
        
    def test_index_with_posts(self):
        """Verifica que se muestran los posts en la página principal"""
        with self.app.app_context():
            admin = User.get_by_email('admin@test.com')
            post = Post(user_id=admin.id, title='Post de prueba', content='Lorem Ipsum')
            post.save()
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Post de prueba', res.data)
        
    def test_redirect_to_login(self):
        """Verifica la redirección a la página de login"""
        res = self.client.get('/admin/')
        self.assertEqual(302, res.status_code)
        self.assertIn('login', res.location)
        
    def test_unauthorized_access_to_admin(self):
        """Verifica que un usuario invitado no puede acceder al área de administración"""
        with self.app.test_client() as c:
            # Obtener el usuario invitado
            user = self.login('guest@test.com', 'guest')
            # Simular la sesión iniciada
            with c.session_transaction() as sess:
                sess['_user_id'] = str(user.id)
            # Luego intentamos acceder al área de admin
            res = c.get('/admin/')
            self.assertEqual(302, res.status_code)  # Redirección al login
            self.assertIn('login', res.location)
        
    def test_authorized_access_to_admin(self):
        """Verifica que un usuario admin puede acceder al área de administración"""
        with self.app.test_client() as c:
            # Obtener el usuario admin
            user = self.login('admin@test.com', 'admin')
            # Simular la sesión iniciada
            with c.session_transaction() as sess:
                sess['_user_id'] = str(user.id)
            # Luego intentamos acceder al área de admin
            res = c.get('/admin/')
            self.assertEqual(200, res.status_code)
            self.assertIn(b'Posts', res.data)
            self.assertIn(b'Usuarios', res.data)

if __name__ == '__main__':
    unittest.main()