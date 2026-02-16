from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form

import pathlib
from time import time
from typing import List
from app.schemas.product import ProductRespons
from app.db.database import LocalSession
from app.models.product import Product, Image


product_router = APIRouter(
    prefix="/products",
    tags=["Products Endpoint"]
)


@product_router.post("",response_model=ProductRespons)             # images: List[UploadFile]=File  -> Upload file bu obyektlar ruycati kelsin File kurinishida
def create_product(
    name : str = Form(min_length=3,max_length=250),
    price : float = Form(gt=0),
    description: str | None = Form(None),
    images: List[UploadFile] = File()
    ):
    
    db = LocalSession()
    
    product = Product(
        name=name,
        price=price,
        description=description
    )
    
    db.add(product)
    db.commit()
    db.refresh(product)
    

    for image in images:
        
        filename = str(pathlib.Path.cwd()) + "/images/" + str(time()) + ".jpeg"   #/home/nodirbek/practic/Fast-Api-requests + /images/ + {uniq bo'lishi keark} + ".jpeg"

        with open(filename,"wb") as f:
            contents = image.file.read()
            f.write(contents)
            
            product_image = Image(product_id = product.id, url = filename)
            db.add(product_image)
            db.commit()
            db.refresh(product_image)
    
    return product
            
        
        
        
            


    