from functools import wraps
from flask import abort, redirect, url_for
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'is_admin', False)
        
        # Si el usuario no está autenticado o no es admin, redireccionar al login
        if not current_user.is_authenticated or not is_admin:
            return redirect(url_for('auth.login'))
        
        return f(*args, **kws)
    return decorated_function
