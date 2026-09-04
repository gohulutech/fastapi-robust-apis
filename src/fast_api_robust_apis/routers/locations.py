from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fast_api_robust_apis.db.session import get_db
from fast_api_robust_apis.crud.location import location_repository

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("/")
def list_locations(db: Session = Depends(get_db)):
    """Retrieve all locations"""
    locations = location_repository.get_all(db)
    return locations
