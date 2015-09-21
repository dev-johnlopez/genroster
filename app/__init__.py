from flask import Flask, url_for, request, jsonify
from flask.ext import excel
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
import itertools
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

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
    	#QBs = Player.query.filter(position='QB')).all()
    	#RBs = Player.query.filter(position='RB')).all()
    	#WRs = Player.query.filter(position='WR')).all()
    	#TEs = Player.query.filter(position='TE')).all()
    	#Ks = Player.query.filter(position='K')).all()
    	#Ds = Team.query.filter.all()
    	players = Player.query.all()
    	teams = Team.query.all()
    	positions = players
    	for team in teams:
    		positions.append(team)
    	print "Creating Combinations"
    	all_combinations = list(itertools.combinations(positions, 5))
    	print "Combinations Created - %s" % len(all_combinations)
    	rosters = []
    	for item in all_combinations:
    		roster_allowed = True
    		if len(filter((lambda roster_spot: roster_spot.position == "QB"), item)) != 1:
    			roster_allowed = False
    		if len(filter((lambda roster_spot: roster_spot.position == "RB"), item)) != 2:
    			roster_allowed = False
    		if len(filter((lambda roster_spot: roster_spot.position == "WR"), item)) != 3:
    			roster_allowed = False
    		if len(filter((lambda roster_spot: roster_spot.position == "TE"), item)) != 1:
    			roster_allowed = False
    		if len(filter((lambda roster_spot: roster_spot.position == "K"), item)) != 1:
    			roster_allowed = False
    		if len(filter((lambda roster_spot: roster_spot.position == "D"), item)) != 1:
    			roster_allowed = False
    		cur_salary = 0
    		for position in item:
    			cur_salary += position.salary
    		if cur_salary > 60000:
    			roster_allowed = False
    		if roster_allowed:
    			rosters.append(item)

        return self.render('analytics_index.html', rosters=rosters)

class ImportView(BaseView):
	@expose('/')
	def index(self):
		return self.render('import_players.html')

	@expose('/players', methods=('GET', 'POST',))
	def doimport(self):
		if request.method == 'POST':
			def player_init_func(row):
				p = Player(row['First Name'], row['Last Name'], row['Position'], row['FPPG'], row['Played'], row['Salary'], row['Injury Indicator'], row['Injury Details'])
				return p
			request.save_book_to_database(field_name='file', session=db.session,
                                      tables=[Player],
                                      initializers=([player_init_func]))
        
		return self.render('success.html')

admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))
admin.add_view(ImportView(name='Import', endpoint='import'))

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
