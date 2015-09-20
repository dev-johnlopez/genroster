from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Player = Table('Player', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255), nullable=False),
    Column('team', String(length=255), nullable=False),
    Column('position', String(length=2), nullable=False),
    Column('fpg', Float(precision=6)),
    Column('salary', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Player'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Player'].drop()
