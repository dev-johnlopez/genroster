from app import app
from app import db
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, event, Boolean, Table
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from datetime import datetime

class Player(db.Model):
	__tablename__ = 'Player'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(255), nullable=False, server_default='')
	last_name = db.Column(db.String(255), nullable=False, server_default='')
	position = db.Column(db.String(255), nullable=False, server_default='')
	fppg = db.Column(db.Float(6))
	played = db.Column(db.Integer)
	salary = db.Column(db.Integer)
	injury_ind = db.Column(db.String(2), nullable=True, server_default='')
	injury_details = db.Column(db.String(255), nullable=True, server_default='')
	team = db.Column(db.String(3), nullable=True, server_default='')
	multiplier = db.Column(db.Float(6))
	#team_id = db.Column(db.Integer, db.ForeignKey('Team.id'))
	starting = db.Column(db.Boolean)

	def __init__(self, first_name, last_name, position, fppg, played, salary, injury_ind, injury_details, starting, team, multiplier):
		self.first_name = first_name
		self.last_name = last_name
		self.position = position
		self.fppg = fppg
		self.played = played
		self.salary = salary
		self.injury_ind = injury_ind
		self.injury_details = injury_details
		self.multiplier = multiplier
		if starting == "Y":
			self.starting = True
		else:
			self.starting = False
		self.team = team

	def __repr__(self):
		return '%s %s' % (self.first_name, self.last_name)

	def getCalculatedFPPG(self):
		return self.fppg * self.multiplier

class Team(db.Model):
	__tablename__ = 'Team'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False, server_default='')
	#players = db.relationship("Player", backref="team")

	def __repr__(self):
		return '%r' % (self.name)
