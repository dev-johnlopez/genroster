from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Team = Table('Team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255), nullable=False),
)

Player = Table('Player', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=255), nullable=False),
    Column('team', VARCHAR(length=255), nullable=False),
    Column('position', VARCHAR(length=2), nullable=False),
    Column('fpg', FLOAT),
    Column('salary', INTEGER),
)

Player = Table('Player', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255), nullable=False),
    Column('fpg', Float(precision=6)),
    Column('salary', Integer),
    Column('team_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Team'].create()
    pre_meta.tables['Player'].columns['position'].drop()
    pre_meta.tables['Player'].columns['team'].drop()
    post_meta.tables['Player'].columns['team_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Team'].drop()
    pre_meta.tables['Player'].columns['position'].create()
    pre_meta.tables['Player'].columns['team'].create()
    post_meta.tables['Player'].columns['team_id'].drop()
