from fastapi import FastAPI, Depends
from models import Products
from postgre_database import session, engine
import postgre_database_models
from sqlalchemy.orm import Session

app = FastAPI()

postgre_database_models.Base.metadata.create_all(bind=engine)


products=[
  Products(id=1, name="jack n' jill",price=50),
  Products(id=2, name="oreos", price=60),
  Products(id=3, name="potato", price=70),
  Products(id=4, name="flakes", price=70)
]

def get_db():
  db = session()
  try:
    yield db
  finally:
    db.commit

def db_init():
  db = session()
  for p in products:
    db.merge(postgre_database_models.Products(**p.model_dump()))

  db.commit()

db_init()

#reads db and display through url
@app.get('/get_all_products')
def get_Products(db: Session = Depends(get_db)):
  all_Products = db.query(postgre_database_models.Products).all()
  return all_Products

@app.get('/get_by_id/{id}')
def get_product(id:int, db: Session =Depends(get_db)):
  prod = db.query(postgre_database_models.Products).filter(postgre_database_models.Products.id == id).first()
  if prod:
    return prod
  return "product not found"
    
@app.delete('/delete_by_id/{id}')
def del_by_id(id:int, db: Session = Depends(get_db)):
  prod = db.query(postgre_database_models.Products).filter(postgre_database_models.Products.id == id).first()
  if prod:
    db.delete(prod)
    db.commit()
    return "successful"
  else:
    return "products not found"
  # for i in range(len(products)):
  #   if products[i].id == id:
  #     del products[i]
  # return products

@app.post('/add')
def add_prod(p:Products, db:Session = Depends(get_db)):
  db.add(postgre_database_models.Products(**p.model_dump()))
  db.commit()
  return p

  # for prod in products:
  #   if prod.id == p.id:
  #     return('Already exist')
  # products.append(p)
  # return products

@app.put('/update/{id}')
def update_prod(id:int, prod:Products, db:Session = Depends(get_db)):
  p = db.query(postgre_database_models.Products).filter(postgre_database_models.Products.id == id).first()
  if p:
    p.name = prod.name
    p.price = prod.price
    db.commit()
    return "prod updated"
  else:
  # for i in range(len(products)):
  #   if products[i].id == id:
  #     products[i] = prod
    return "not found"

