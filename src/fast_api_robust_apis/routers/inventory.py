from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fast_api_robust_apis.db.session import get_db
from fast_api_robust_apis.crud.inventory import inventory_repository
from fast_api_robust_apis.schemas.inventory import InventoryUpdate

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/by-product/{product_id}")
def get_inventory_by_product(product_id: int, db: Session = Depends(get_db)):
    """Retrieve all inventory items for a specific product"""
    inventory_items = inventory_repository.get_by_product(db, product_id)
    result = []
    for inventory_item, location in inventory_items:
        result.append(
            {
                "quantity": inventory_item.quantity,
                "reorder_point": inventory_item.reorder_point,
                "location_name": location.name,
                "location_id": location.id,
                "product_id": inventory_item.product_id,
                "in_stock": inventory_item.quantity > 0,
                "needs_reorder": inventory_item.quantity < inventory_item.reorder_point,
            }
        )
    return result


@router.get("/by-location/{location_id}")
def get_inventory_by_location(location_id: int, db: Session = Depends(get_db)):
    """Retrieve all inventory items for a specific location"""
    inventory_items = inventory_repository.get_by_location(db, location_id)
    result = []
    for inventory_item, product in inventory_items:
        result.append(
            {
                "quantity": inventory_item.quantity,
                "reorder_point": inventory_item.reorder_point,
                "product_name": product.name,
                "product_id": product.id,
                "product_id": inventory_item.product_id,
                "in_stock": inventory_item.quantity > 0,
                "needs_reorder": inventory_item.quantity < inventory_item.reorder_point,
            }
        )
    return result


@router.put("/")
def update_inventory(update: InventoryUpdate, db: Session = Depends(get_db)):
    """Update inventory stock levels (add or remove stock)"""
    result = inventory_repository.update_stock(
        db,
        product_id=update.product_id,
        location_id=update.location_id,
        quantity_change=update.quantity_change,
    )
