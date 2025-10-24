import os

from flask import send_from_directory
from app import create_app

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


@app.route('/media/posts/<filename>')
def media_posts(filename):
    """Serve post images from media directory"""
    return send_from_directory(app.config['POSTS_IMAGES_DIR'], filename)


if __name__ == '__main__':
    app.run()
