import sys
from sqlalchemy import Column, Integer, Text, DateTime, Sequence
from sqlalchemy.sql.functions import current_timestamp
from . database import ENGINE, Base


class Tag(Base):
    __tablename__ = 'tags'
    id = Column('id', Integer, Sequence('tags_id_seq'), primary_key=True)
    keyword = Column('keyword', Text)
    count = Column('count', Integer)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())

def main(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
    main(sys.argv)
