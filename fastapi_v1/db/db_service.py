from db import db_connection as _db
from db import models as _models

def _add_table():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

