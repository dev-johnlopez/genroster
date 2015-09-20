from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
#import stripe


import os

#stripe_keys = {
#   'secret_key': 'sk_test_jFav95nmL7CuiqTq1r3helDT',
#    'publishable_key': 'pk_test_6kN4KpOzRqZww0k55vsbM0Pa'
#}

#stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import models
from models import Player
from models import Team
admin = Admin(app, name='Generate Roster', template_mode='bootstrap3')
admin.add_view(ModelView(Player, db.session))
admin.add_view(ModelView(Team, db.session))

from app import views


#from .controllers.factory import LoadFactory

from config import basedir

#if not app.debug and os.environ.get('HEROKU') is None:
#    import logging
#    from logging.handlers import RotatingFileHandler
#    file_handler = RotatingFileHandler('tmp/genroster.log', 'a', 1 * 1024 * 1024, 10)
#    file_handler.setLevel(logging.INFO)
#    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#    app.logger.addHandler(file_handler)
#    app.logger.setLevel(logging.INFO)
#    app.logger.info('TMS startup')

#if os.environ.get('HEROKU') is not None:
#    import logging
#    stream_handler = logging.StreamHandler()
#    app.logger.addHandler(stream_handler)
#    app.logger.setLevel(logging.INFO)
#    app.logger.info('TMS startup')

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['f_static'] = (
    lambda filename: url_for('static', filename = filename)
)
