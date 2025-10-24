import logging

from smtplib import SMTPException
from threading import Thread

from flask import current_app
from flask_mail import Message

from app import mail

logger = logging.getLogger(__name__)


def _send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except SMTPException as e:
            logger.error(f'Error sending email: {e}')


def send_email(subject, recipients, text_body, html_body, sender=None):
    if sender is None:
        sender = current_app.config['DONT_REPLY_FROM_EMAIL']
    
    msg = Message(subject, recipients=recipients, sender=sender)
    msg.body = text_body
    msg.html = html_body
    
    Thread(target=_send_async_email, args=(current_app._get_current_object(), msg)).start()
