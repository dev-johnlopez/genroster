from app import app
from app import db
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, event, Boolean, Table
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from datetime import datetime

class Player(db.Model):
	__tablename__ = 'Player'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False, server_default='')
	position = db.Column(db.String(255), nullable=False, server_default='')
	fpg = db.Column(db.Float(6))
	salary = db.Column(db.Integer)
	team_id = db.Column(db.Integer, db.ForeignKey('Team.id'))

	def __repr__(self):
		return '%r' % (self.name)

class Team(db.Model):
	__tablename__ = 'Team'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False, server_default='')
	players = db.relationship("Player", backref="team")

	def __repr__(self):
		return '%r' % (self.name)
