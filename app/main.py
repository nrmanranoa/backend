from typing import Optional, List
from fastapi import FastAPI
from fastapi import FastAPI, status, Depends, HTTPException
from . import models
from sqlalchemy.orm import Session
from .database import get_db, engine
from . import schemas
from . import utils
from fastapi.middleware.cors import CORSMiddleware

#code that creates the tables
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Message": "Hello world!"}

@app.post("/material", status_code=status.HTTP_201_CREATED, response_model=schemas.Material)
def post_material(post: schemas.PostCreate, db: Session = Depends(get_db)):
    created_material = models.Material(
        **post.dict(),
        elements=utils.separate_elements(post.formula)
    )
    db.add(created_material)
    db.commit()
    db.refresh(created_material)

    return created_material

@app.get("/material/{id}", response_model=schemas.GetMaterial)
def get_material(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Material).filter_by(id=str(id)).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Material id {id} was not found")
    return post

@app.get("/search", response_model=List[schemas.GetMaterial])
def search_materials(db: Session = Depends(get_db), max_density: Optional[float] = None, 
min_density: Optional[float] = None, include_elements: Optional[str] = None, exclude_elements: Optional[str] = None):
    max_density = max_density if max_density is not None else False
    min_density = min_density if min_density is not None else False
    include_elements = include_elements.replace(" ", "").split(",") if include_elements is not None else False
    exclude_elements = exclude_elements.replace(" ", "").split(",") if exclude_elements is not None else False

    print(max_density)
    print(min_density)

    materials = db.query(models.Material)
    
    if min_density is not None:
        materials = materials.filter(models.Material.density >= min_density)
    if max_density is not None:
        materials = materials.filter(models.Material.density <= max_density)
    if include_elements:
        materials = materials.filter(models.Material.elements.contains(include_elements))
    if exclude_elements:
        materials = materials.filter(~models.Material.elements.contains(exclude_elements))
    
    result = materials.all()

    return materials


    print(max_density)
    print(min_density)
    print(include_elements)
    print(exclude_elements)