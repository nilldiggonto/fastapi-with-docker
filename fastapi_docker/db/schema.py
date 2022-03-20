from unicodedata import name
from matplotlib.pyplot import title
from pydantic import BaseModel

class BookSchema(BaseModel):
    title   :   str
    rating  :   int
    authord_id : int

    class Config:
        orm_mode = True


class AuthorSchema(BaseModel):
    name    :   str
    age     :   str

    class Config:
        orm_mode = True