import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DB_URL = "postgresql://nill:nill1234@localhost/fastapi_database"

engine = _sql.create_engine(DB_URL)

SessionLocal = _orm.sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = _declarative.declarative_base()