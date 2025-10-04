from fastapi import FastAPI, Depends
from models import Product
from fastapi.middleware.cors import CORSMiddleware
from postgre_database import session, engine
import postgre_database_models
from sqlalchemy.orm import Session

app = FastAPI()

#for the frontend to merge with the backend
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

#creates the tables using the base model
postgre_database_models.Base.metadata.create_all(bind=engine)


#products that is read and displayed
products=[
  Product(id=1, name="jack n' jill", description='vanilla ', price=50, quantity=4),
  Product(id=2, name="oreos", description='choco', price=60, quantity=4),
  Product(id=3, name="potato", description='vanilla fruit', price=70, quantity=4),
  Product(id=4, name="flakes", description='vanilla choco', price=70, quantity=4)
]

# create a session function for new db sessions
def get_db():
  db = session()
  try:
    yield db
  finally:
    db.close()

#function that reads the products list and insert it into the db
def db_init():
  db = session()
  for p in products:
    db.merge(postgre_database_models.Product(**p.model_dump())) #converts p to dict and then to key and value pair for Product

  db.commit()

db_init()

#reads db and display through url
@app.get('/products')
def get_Products(db: Session = Depends(get_db)):
  all_Products = db.query(postgre_database_models.Product).all()
  return all_Products

#get product by query db to find matching id
@app.get('/products/{id}')
def get_product(id:int, db: Session =Depends(get_db)):
  prod = db.query(postgre_database_models.Product).filter(postgre_database_models.Product.id == id).first()
  if prod:
    return prod
  return "product not found"
    
@app.delete('/products/{id}')
def del_by_id(id:int, db: Session = Depends(get_db)):
  prod = db.query(postgre_database_models.Product).filter(postgre_database_models.Product.id == id).first()
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

@app.post('/products')
def add_prod(p:Product, db:Session = Depends(get_db)):
  db.add(postgre_database_models.Product(**p.model_dump()))
  db.commit()
  return p

  # for prod in products:
  #   if prod.id == p.id:
  #     return('Already exist')
  # products.append(p)
  # return products

@app.put('/products')
def update_prod(id:int, prod:Product, db:Session = Depends(get_db)):
  p = db.query(postgre_database_models.Product).filter(postgre_database_models.Product.id == id).first()
  if p:
    p.name = prod.name
    p.description = prod.description
    p.price = prod.price
    p.quantity = prod.quantity
    db.commit()
    return "prod updated"
  else:
  # for i in range(len(products)):
  #   if products[i].id == id:
  #     products[i] = prod
    return "not found"

