from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'postgresql://%s:%s@%s/%s' % (
    "postgres",
    "",
    "127.0.0.1",
    "postgres",
)

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
