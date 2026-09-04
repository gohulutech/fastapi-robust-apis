from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re


class ProductCreate(BaseModel):
    """Schema for creating a new product"""

    name: str = (Field(..., min_length=1, max_length=100),)
    description: Optional[str] = None
    sku: str = Field(..., min_length=5, max_length=9)
    price: float = Field(..., gt=0)

    @field_validator("sku")
    def validate_sku(cls, v):
        """Validate SKU format (e.g., TECH-001)"""
        if not re.match(r"^[A-Z]+-\d+$", v):
            raise ValueError("SKU must be in format CATEGORY-NUMBER (e.g., TECH-001)")
        return v.upper()

    @field_validator("name")
    def valudate_name(cls, v):
        """Validate name doesn't contain problematic characters"""
        forbidden_chars = ["@", "#", "$", "%", "&"]
        for char in forbidden_chars:
            if char in v:
                raise ValueError(f"Name cannot contain special character '{char}'")
            return v

    @field_validator("price")
    def validate_price(cls, v):
        """Additional price validation"""
        v = round(v, 2)
        if v > 10000:
            raise ValueError("Price cannot exceed $10,000")
        return v
