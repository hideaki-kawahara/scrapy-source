import sys
from sqlalchemy import Column, Integer, Text, DateTime, Sequence
from sqlalchemy.sql.functions import current_timestamp
from database import ENGINE, Base

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column('id', Integer, Sequence('recipes_id_seq'), primary_key=True)
    site_url = Column('site_url', Text)
    title = Column('title', Text)
    detail = Column('detail', Text)
    cooking_time = Column('cooking_time', Text)
    budget = Column('budget', Text)
    ingredient = Column('ingredient', Text)
    how_to_make = Column('how_to_make', Text)
    tip = Column('tip', Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())

def main(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
    main(sys.argv)
