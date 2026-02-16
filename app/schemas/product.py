from pydantic import BaseModel


class Images(BaseModel):
    id: int
    url : str
    
    class Config:
        from_attributes = True
        

class ProductRespons(BaseModel):
    id : int
    name : str 
    description: str | None = None
    price: float
    images: list[Images]
    
    class Config:
        from_attributes = True
         
        