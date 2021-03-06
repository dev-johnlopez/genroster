from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
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
    Column('team_id', Integer),
    Column('starting', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Player'].columns['starting'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Player'].columns['starting'].drop()
