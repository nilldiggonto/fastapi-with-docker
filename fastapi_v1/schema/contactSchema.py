import datetime as _dt
import email
from pydantic import BaseModel

class _BaseContact(BaseModel):
    first_name  :   str
    last_name   :   str
    email       :   str
    phone_number    :   str

class Contact(_BaseContact):
    id  :   int
    created_at  :   _dt.datetime

    class Config:
        orm_model = True

class CreateContact(_BaseContact):
    pass