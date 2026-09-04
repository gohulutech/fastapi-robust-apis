from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fast_api_robust_apis.db.session import get_db
from fast_api_robust_apis.crud.product import product_repository

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    """Retrieve all products"""
    products = product_repository.get_all(db)
    return products
