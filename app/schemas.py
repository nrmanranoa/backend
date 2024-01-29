from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    formula: str
    density: float

class PostCreate(PostBase):
    pass

class GetMaterial(BaseModel):
    formula: str
    density: float

class Material(BaseModel):
    id: int

class SearchMaterial(BaseModel):
    min_density: Optional[float] = None
    max_density: Optional[float] = None
    include_elements: Optional[str] = None
    exclude_elements: Optional[str] = None