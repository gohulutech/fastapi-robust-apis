from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fast_api_robust_apis.db.session import get_db
from fast_api_robust_apis.crud.product import product_repository

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def list_products(
    search: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """Retrieve products with optional search and pagination"""
    if search:
        return product_repository.search(db, search, skip=skip, limit=limit)
    return product_repository.get_all(db, skip=skip, limit=limit)
