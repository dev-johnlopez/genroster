from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Player = Table('Player', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=255), nullable=False),
    Column('last_name', VARCHAR(length=255), nullable=False),
    Column('position', VARCHAR(length=255), nullable=False),
    Column('fppg', FLOAT),
    Column('salary', INTEGER),
    Column('injury_ind', VARCHAR(length=2)),
    Column('injury_details', VARCHAR(length=255)),
    Column('team_id', INTEGER),
    Column('played', INTEGER),
    Column('starting', BOOLEAN),
)

Player = Table('Player', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=255), nullable=False),
    Column('last_name', String(length=255), nullable=False),
    Column('position', String(length=255), nullable=False),
    Column('fppg', Float(precision=6)),
    Column('played', Integer),
    Column('salary', Integer),
    Column('injury_ind', String(length=2)),
    Column('injury_details', String(length=255)),
    Column('team', String(length=3)),
    Column('starting', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Player'].columns['team_id'].drop()
    post_meta.tables['Player'].columns['team'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Player'].columns['team_id'].create()
    post_meta.tables['Player'].columns['team'].drop()
