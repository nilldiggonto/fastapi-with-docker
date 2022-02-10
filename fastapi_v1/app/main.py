import fastapi as _fastapi
from fastapi.param_functions import Body
# from typing import TYPE_CHECKING,List
from db.db_service import get_db
from schema import contactSchema as _contact
from db.models import Contact
from sqlalchemy.orm import Session


app = _fastapi.FastAPI()

#request:dict=Body(...)
@app.post('/api/contact')
async def create_contact(request:_contact.CreateContact,db:Session = _fastapi.Depends(get_db)):
    c   =   Contact(**request.dict())
    db.add(c)
    db.commit()
    db.refresh(c)
    return {'status':'Contact Created'}

@app.get('/api/contact/list')
async def contact_list(db:Session = _fastapi.Depends(get_db)):
    contacts = db.query(Contact)
    data = [{'first_name':c.first_name,'email':c.email} for c in contacts]
    return data

