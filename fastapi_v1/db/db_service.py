import db_connection as _db
import models as _models

def _add_table():
    return _db.Base.metadata.create_all(bind=_db.engine)