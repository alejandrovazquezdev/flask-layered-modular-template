# Miniblog - Flask Blog Application

<p align="center">
  <img src="https://img.shields.io/badge/Flask-3.0.0-green?style=for-the-badge&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlite" alt="SQLAlchemy">
</p>

<p align="center">
  <strong>A complete, production-ready blog application built with Flask</strong>
</p>

<p align="center">
  Una aplicación web completa de blog desarrollada con Flask siguiendo las mejores prácticas y arquitectura modular.
</p>

---

## Acerca del Proyecto

**Miniblog** es una aplicación de blogging completa que implementa:

- **Autenticación y autorización** de usuarios con roles
- **CRUD completo** de posts (crear, leer, actualizar, eliminar)
- **Gestión de imágenes** con subida y almacenamiento seguro
- **Sistema de usuarios** con permisos diferenciados
- **Envío de emails** asíncrono
- **Paginación** de contenido
- **Tests unitarios** completos
- **Migraciones de base de datos** con Alembic

---

## Características

### Para Visitantes
- Ver lista de posts publicados
- Leer posts completos con imágenes
- Navegación paginada
- URLs amigables (SEO-friendly)

### Para Usuarios Registrados
- Crear cuenta y autenticarse
- Sesiones persistentes
- Email de bienvenida

### Para Administradores
- Panel de administración completo
- Crear, editar y eliminar posts
- Subir imágenes de cabecera (JPG/PNG)
- Gestionar usuarios y permisos
- Generación automática de slugs
- Manejo de slugs duplicados

---

## Arquitectura

El proyecto implementa una **arquitectura modular en capas** utilizando:

- **App Factory Pattern** - Inicialización flexible de la aplicación
- **Blueprint Pattern** - Organización modular del código
- **Repository Pattern** - Abstracción de la capa de datos
- **Decorator Pattern** - Control de acceso y autorización

### Estructura del Proyecto

```
flask-layered-modular-template/
│
├── app/                          # Aplicación principal
│   ├── __init__.py              # Factory function
│   ├── models.py                # Modelo Post
│   │
│   ├── admin/                   # Blueprint admin
│   │   ├── routes.py           # CRUD de posts
│   │   ├── forms.py            # Formularios
│   │   └── templates/          # Templates admin
│   │
│   ├── auth/                    # Blueprint autenticación
│   │   ├── routes.py           # Login/Signup/Logout
│   │   ├── models.py           # Modelo User
│   │   ├── decorators.py       # @admin_required
│   │   └── templates/          # Templates auth
│   │
│   ├── public/                  # Blueprint público
│   │   ├── routes.py           # Lista y vista de posts
│   │   └── templates/          # Templates públicos
│   │
│   ├── common/                  # Utilidades compartidas
│   │   ├── mail.py             # Sistema de emails
│   │   └── filters.py          # Filtros Jinja2
│   │
│   ├── templates/               # Templates base
│   │   ├── base_template.html
│   │   ├── 404.html
│   │   └── 500.html
│   │
│   └── static/                  # Archivos estáticos
│       └── base.css
│
├── config/                       # Configuraciones
│   ├── default.py               # Config base
│   ├── local.py                 # Desarrollo local
│   ├── dev.py                   # Desarrollo
│   ├── testing.py               # Tests
│   └── prod.py                  # Producción
│
├── migrations/                   # Migraciones Alembic
├── tests/                        # Tests unitarios
├── instance/                     # Archivos locales (no en git)
├── media/                        # Archivos subidos (no en git)
│
├── entrypoint.py                 # Punto de entrada
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

---

## Inicio Rápido

### Prerequisitos

- Python 3.11 o superior
- pip
- virtualenv o venv

### Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/alejandrovazquezdev/flask-layered-modular-template.git
cd flask-layered-modular-template
```

2. **Crear entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

```bash
export APP_SETTINGS_MODULE='config.local'
export FLASK_APP="entrypoint.py:create_app('config.local')"
export FLASK_DEBUG=1
```

O agregar al final de `venv/bin/activate`:

```bash
export APP_SETTINGS_MODULE='config.local'
export FLASK_APP="entrypoint.py:create_app('config.local')"
export FLASK_DEBUG=1
```

5. **Inicializar la base de datos**

```bash
# Crear migraciones
flask db init  # (solo primera vez)

# Aplicar migraciones
flask db upgrade

# Crear tablas desde Python (alternativa)
python
>>> from entrypoint import app
>>> from app import db
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

6. **Crear usuario administrador**

```bash
python
>>> from entrypoint import app
>>> from app.auth.models import User
>>> from app import db
>>> app.app_context().push()
>>> admin = User()
>>> admin.name = "Admin"
>>> admin.email = "admin@example.com"
>>> admin.password = "admin123"
>>> admin.is_admin = True
>>> db.session.add(admin)
>>> db.session.commit()
>>> exit()
```

7. **Ejecutar la aplicación**

```bash
flask run
```

La aplicación estará disponible en `http://localhost:5000`

---

## Uso

### Área Pública

- **Home:** `http://localhost:5000/`
  - Lista de posts con paginación

- **Ver post:** `http://localhost:5000/p/<slug>/`
  - Post completo con imagen

### Autenticación

- **Login:** `http://localhost:5000/auth/login`
- **Registro:** `http://localhost:5000/auth/signup/`
- **Logout:** `http://localhost:5000/auth/logout`

### Panel de Administración

- **Dashboard:** `http://localhost:5000/admin/`
  - Lista de posts con opciones de editar/eliminar

- **Crear post:** `http://localhost:5000/admin/post/`
  - Formulario con título, contenido e imagen

- **Gestionar usuarios:** `http://localhost:5000/admin/users/`
  - Asignar/quitar permisos de admin

---

## Testing

Ejecutar todos los tests:

```bash
python -m unittest discover -v
```

Ejecutar tests específicos:

```bash
# Tests del modelo Post
python -m unittest tests.test_post_model -v

# Tests del cliente web
python -m unittest tests.test_blog_client -v
```

Con cobertura:

```bash
pytest --cov=app tests/
```

---

## Configuración

### Configuración por Entornos

El proyecto soporta múltiples entornos:

- `config.local` - Desarrollo local
- `config.dev` - Desarrollo
- `config.testing` - Tests (SQLite in-memory)
- `config.staging` - Pre-producción
- `config.prod` - Producción

Cambiar entorno:

```bash
export APP_SETTINGS_MODULE='config.prod'
```

### Variables de Configuración Importantes

**config/default.py:**

```python
SECRET_KEY = '...'                    # Para sesiones
SQLALCHEMY_DATABASE_URI = '...'       # Conexión BD
MEDIA_DIR = join(BASE_DIR, 'media')   # Directorio de archivos
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')
ITEMS_PER_PAGE = 3                    # Posts por página

# Email configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'tu-email@gmail.com'
MAIL_PASSWORD = 'tu-password'
MAIL_USE_TLS = True
```

---

## Seguridad

El proyecto implementa múltiples capas de seguridad:

- **Flask-Login** - Gestión de sesiones
- **CSRF Protection** - Tokens en formularios (Flask-WTF)
- **Password Hashing** - PBKDF2 (Werkzeug)
- **Secure Filenames** - Sanitización de nombres de archivo
- **File Validation** - Solo JPG/PNG permitidos
- **Role-Based Access** - Decoradores `@login_required` y `@admin_required`

---

## Tecnologías Utilizadas

### Core
- **Flask 3.0.0** - Framework web
- **SQLAlchemy 2.0.44** - ORM
- **Jinja2 3.1.6** - Motor de templates

### Extensiones Flask
- **Flask-Login 0.6.3** - Autenticación
- **Flask-WTF 1.2.2** - Formularios y CSRF
- **Flask-SQLAlchemy 3.1.1** - Integración SQLAlchemy
- **Flask-Migrate 4.0.7** - Migraciones de BD
- **Flask-Mail 0.9.1** - Envío de emails

### Utilidades
- **python-slugify 8.0.4** - Generación de slugs
- **Werkzeug 3.1.3** - Utilidades WSGI
- **Alembic 1.13.1** - Migraciones de BD

### Testing
- **pytest 8.1.1** - Framework de tests
- **pytest-cov 5.0.0** - Cobertura de código
- **Flask-Testing 0.8.1** - Utilidades de testing

---

## Base de Datos

### Modelos

**User (blog_user)**
- `id` - Integer (PK)
- `name` - String(80)
- `email` - String(256), único
- `password` - String(128), hasheado
- `is_admin` - Boolean

**Post**
- `id` - Integer (PK)
- `user_id` - Integer (FK → blog_user.id)
- `title` - String(256)
- `title_slug` - String(256), único
- `content` - Text
- `created` - DateTime, auto
- `image_name` - String (opcional)

### Migraciones

```bash
# Crear migración
flask db migrate -m "descripción del cambio"

# Aplicar migraciones
flask db upgrade

# Revertir migración
flask db downgrade

# Ver estado actual
flask db current

# Ver historial
flask db history
```

---

## Screenshots

### Página Principal
```
┌─────────────────────────────────────┐
│         Miniblog - Home             │
├─────────────────────────────────────┤
│ • Tutorial Flask (24/10/2025)       │
│ • Aprendiendo Python (23/10/2025)   │
│ • Guía de Git (22/10/2025)          │
├─────────────────────────────────────┤
│     [1] 2 3 ... 10                  │
└─────────────────────────────────────┘
```

### Vista de Post
```
┌─────────────────────────────────────┐
│    Tutorial de Flask                │
├─────────────────────────────────────┤
│    23 de 10 de 2025                 │
├─────────────────────────────────────┤
│    [Imagen de cabecera]             │
├─────────────────────────────────────┤
│ Flask es un framework...            │
│                                     │
│ [Contenido completo]                │
└─────────────────────────────────────┘
```

### Panel Admin
```
┌─────────────────────────────────────┐
│    Panel de Administración          │
│    [+ Crear Post]                   │
├─────────────────────────────────────┤
│ 1. Tutorial Flask                   │
│    [Editar] [Eliminar]              │
├─────────────────────────────────────┤
│ 2. Aprendiendo Python               │
│    [Editar] [Eliminar]              │
└─────────────────────────────────────┘
```

---

## Deployment, No implmentado

### Producción con Gunicorn + Nginx

1. **Instalar Gunicorn**

```bash
pip install gunicorn
```

2. **Ejecutar con Gunicorn**

```bash
gunicorn -w 4 -b 0.0.0.0:8000 "entrypoint:create_app('config.prod')"
```

3. **Configurar Nginx**

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /ruta/a/app/static;
    }

    location /media {
        alias /ruta/a/media;
    }
}
```

### Variables de Entorno en Producción

```bash
export APP_SETTINGS_MODULE='config.prod'
export SECRET_KEY='tu-secret-key-seguro'
export DATABASE_URL='postgresql://user:pass@localhost/dbname'
export MAIL_SERVER='smtp.tu-servidor.com'
export MAIL_USERNAME='tu-email'
export MAIL_PASSWORD='tu-password'
```

---

## Documentación Adicional

- [Tutorial Completo en j2logo.com](https://j2logo.com/tutorial-flask-espanol/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)

---

## Autor

**Alejandro Vázquez**

- GitHub: [@alejandrovazquezdev](https://github.com/alejandrovazquezdev)
- Proyecto: [flask-layered-modular-template](https://github.com/alejandrovazquezdev/flask-layered-modular-template)

---

## Agradecimientos

- Tutorial base de [j2logo.com](https://j2logo.com/)
- Comunidad de Flask
- Documentación oficial de Flask y extensiones
- Todos los contribuidores

---

## Estado del Proyecto

- **16 lecciones completadas**
- **~850 líneas de código Python**
- **13 templates HTML**
- **7 tests unitarios**
- **2 migraciones de base de datos**
- **100% funcional**

**Última actualización:** 24 de octubre de 2025

---

<p align="center">
  Hecho con usando Flask
</p>

<p align="center">
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.sqlalchemy.org/">
    <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLAlchemy">
  </a>
</p>
