from fastapi import FastAPI
from models import Products
from database import session, engine
import database_models
# from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


products=[
  Products(id=1, name="jack n' jill",price=50),
  Products(id=2, name="oreos", price=60),
  Products(id=3, name="potato", price=70)
]

@app.get('/get_all_products')
def get_Products():
  # db = session()
  # db
  return products

@app.get('/get_by_id/{id}')
def get_product(id:int):
  for p in products:
    if p.id == id:
      return p
    
@app.delete('/delete_by_id/{id}')
def del_by_id(id:int):
  for i in range(len(products)):
    if products[i].id == id:
      del products[i]
  return products

@app.post('/add')
def add_prod(p:Products):
  for prod in products:
    if prod.id == p.id:
      return('Already exist')
  products.append(p)
  return products

@app.put('/update/{id}')
def update_prod(id:int, prod:Products):
  for i in range(len(products)):
    if products[i].id == id:
      products[i] = prod
  return products

