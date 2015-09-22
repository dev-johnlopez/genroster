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
    	QBs = list(Player.query.filter_by(position='QB').all())
        qbs = list(filter((lambda player: player.starting == True), QBs))
        print "QB Sorted Length: %s" % len(qbs)
    	RBs = list(Player.query.filter_by(position='RB').all())
        rbs = list(filter((lambda player: player.starting == True), RBs))
        print "RB Sorted Length: %s" % len(rbs)
    	WRs = list(Player.query.filter_by(position='WR').all())
        wrs = list(filter((lambda player: player.starting == True), WRs))
        print "WR Sorted Length: %s" % len(wrs)
    	TEs = list(Player.query.filter_by(position='TE').all())
        tes = list(filter((lambda player: player.starting == True), TEs))
        print "TE Sorted Length: %s" % len(tes)
    	Ks = list(Player.query.filter_by(position='K').all())
        ks = list(filter((lambda player: player.starting == True), Ks))
        print "K Sorted Length: %s" % len(ks)
    	ds = list(Player.query.filter_by(position='D').all())
        print "D Sorted Length: %s" % len(ds)

        #QBs = list(Player.query.filter((Player.position == 'QB') and (Player.injury_ind == '')))
        #RBs = list(Player.query.filter((Player.position == 'RB') and (Player.injury_ind == '')))
        ##WRs = list(Player.query.filter_by(position = 'WR', injury_ind = ''))
        #TEs = list(Player.query.filter((Player.position == 'TE') and (Player.injury_ind == '')))
        #Ks = list(Player.query.filter((Player.position == 'K') and (Player.injury_ind == '')))
        #Ds = list(Player.query.filter_by(position='D').all())
    	#players = Player.query.all()
    	#teams = Team.query.all()
    	#positions = players
    	#for team in teams:
    	#	positions.append(team)
        qb = list(itertools.combinations(qbs, 1))
    	print "Created QB Combos - %s" % len(qb)
        rb = list(itertools.combinations(rbs, 2))
        
        #valid_rb_combos = []
        #for rb_combo in rb:
        #    if rb_combo[0].team != rb_combo[1].team:
        #        valid_rb_combos.append([rb_combo[0].fppg + rb_combo[1].fppg, rb_combo])

        #total_combos = sorted(valid_rb_combos, key=lambda combo: combo[0], reverse=True)
        #remaining_rb_combos = []
        #for index, combo in enumerate(total_combos):
        #    if index < len(total_combos)/3:
        #        remaining_rb_combos.append(combo[1])
                #print combo

        #rb = remaining_rb_combos

        print "Created RB Combos - %s" % len(rb)
        wr = list(itertools.combinations(wrs, 3))
        #valid_wr_combos = []
        #for index, wr_combo in enumerate(wr):
        #    if wr_combo[0].team != wr_combo[1].team:
        #        if wr_combo[2].team != wr_combo[0].team:
        #            valid_wr_combos.append([wr_combo[0].fppg + wr_combo[1].fppg + wr_combo[2].fppg, wr_combo])
            #print wr_combo[0].fppg + wr_combo[1].fppg + wr_combo[2].fppg
        #total_combos = sorted(valid_wr_combos, key=lambda combo: combo[0], reverse=True)
        #remaining_wr_combos = []
        #for index, combo in enumerate(total_combos):
        #    if index < len(total_combos)/3:
        #        remaining_wr_combos.append(combo[1])
        #        #print combo
        #wr = remaining_wr_combos

        print "Created WR Combos - %s" % len(wr)
        te = list(itertools.combinations(tes, 1))
        print "Created TE Combos - %s" % len(te)
        k = list(itertools.combinations(ks, 1))
        print "Created K Combos - %s" % len(k)
        d = list(itertools.combinations(ds, 1))
        print "Created D Combos - %s" % len(d)
        combine_lists = [qb, rb, wr, te, k, d]
        combos = list(itertools.product(*combine_lists))
        print "combos created"

        print len(qb) * len(rb) * len(wr) * len(te) * len(k) * len(d)



        #for item in wr:
        #    print item
        #for q in qb:
        #    for r in rb:
        #        for w in wr:
        #            for t in te:
        #                for kicker in k:
        #                    for defense in d:
        #                        #print roster_num
        #                        roster_num += 1
        #                        roster = [q, r, w, t, kicker, defense]
        #                        print roster
        #                        possible_rosters.append(roster)
       # print wrs
        #possible_rosters = []
        #for qb in QBs:
        #    roster = []
        #    cur_salary = 0
        #    roster.append(qb)
        #    cur_salary = qb.salary
        #    for rb_tuple in rbs:
        #        for rb in rb_tuple:
        #            cur_salary += rb.salary


    	all_combinations = combos
        print all_combinations
    	print "Combinations Created - %s" % len(all_combinations)
    	rosters = []
        for item in all_combinations:
            cur_salary = item[0][0].salary + item[1][0].salary + item[1][1].salary + item[2][0].salary + item[2][1].salary + item[2][2].salary + item[3][0].salary + item[4][0].salary + item[5][0].salary
            print cur_salary
            if cur_salary <= 60000:
                print "In roster append"
                fppg = 0
                fppg += item[0][0].fppg
                fppg += item[1][0].fppg + item[1][1].fppg
                fppg += item[2][0].fppg + item[2][1].fppg + item[2][2].fppg
                fppg += item[3][0].fppg
                fppg += item[4][0].fppg
                fppg += item[5][0].fppg
                rosters.append([item[0][0], item[1][0], item[1][1], item[2][0], item[2][1], item[2][2], item[3][0], item[4][0], item[5][0], fppg])
        sorted_rosters = sorted(rosters, key=lambda combo: combo[9], reverse=True)
        return self.render('analytics_index.html', rosters=[sorted_rosters[:25]])

class ImportView(BaseView):
    @expose('/')
    def index(self):
        return self.render('import_players.html')

    @expose('/players', methods=('GET', 'POST',))
    def doimport(self):
        if request.method == 'POST':
            players = Player.query.all()
            for player in players:
                print "Deleting %s" % player
                db.session.delete(player)
                db.session.commit()    
            def player_init_func(row):
                p = Player(row['First Name'], row['Last Name'], row['Position'], row['FPPG'], row['Played'], row['Salary'], row['Injury Indicator'], row['Injury Details'], row['Play'], row['Team'])
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
