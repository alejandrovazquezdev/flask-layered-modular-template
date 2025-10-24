import logging

from flask import abort, render_template, current_app, request

from app.models import Post
from . import public_bp

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    current_app.logger.info('Mostrando los posts del blog')
    logger.info('Mostrando los posts del blog')
    page = int(request.args.get('page', 1))
    per_page = current_app.config['ITEMS_PER_PAGE']
    post_pagination = Post.all_paginated(page, per_page)
    return render_template("public/index.html", post_pagination=post_pagination)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    logger.info('Mostrando un post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if post is None:
        logger.info(f'El post {slug} no existe')
        abort(404)
    return render_template("public/post_view.html", post=post)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)
