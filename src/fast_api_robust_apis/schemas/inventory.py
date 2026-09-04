from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional


class InventoryUpdate(BaseModel):
    """Schema for updating inventory stock levels"""

    product_id: int = Field(..., gt=0)
    location_id: int = Field(..., gt=0)
    quantity_change: int
    reorder_point: Optional[int] = Field(None, ge=0)
    reason: Optional[str] = None

    @field_validator("quantity_change")
    def validate_quantity_change(cls, v):
        """Validate quantity change is reasonable"""
        # Limit single transaction size to prevent errors
        if abs(v) > 100000:
            raise ValueError(
                "Quantity change cannot exceeed 1000 units in a single operation"
            )
        return v

    @model_validator(mode="after")
    def validate_inventory_operations(self):
        """Validate business rules across multiple files"""
        # For significant stock reductions, require a reson
        if self.quantity_change and self.quantity_change < -50 and not self.reason:
            raise ValueError("Stock reductions of more than 50 units require a reson")

        # For extremely large changes in either direction, require detailed reason
        if (
            self.quantity_change
            and abs(self.quantity_change) > 200
            and (not self.reason or len(self.reason) < 20)
        ):
            raise ValueError(
                "Changes of more than 200 units require a detailed reason (at least 20 characters)"
            )

        return self
