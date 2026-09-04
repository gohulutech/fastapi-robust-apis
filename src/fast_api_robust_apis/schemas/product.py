from pydantic import BaseModel, Field
from typing import Optional


class ProductCreate(BaseModel):
    """Schema for creating a new product"""

    name: str = (Field(..., min_length=1, max_length=100),)
    description: Optional[str] = None
    sku: str = Field(..., min_length=5, max_length=9)
    price: float = Field(..., gt=0)
