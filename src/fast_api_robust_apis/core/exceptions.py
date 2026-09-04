class InventoryError(Exception):
    """Base exception class for inventory operations"""

    status_code = 500

    def __init__(self, message: str, details: dict = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class RecordNotFoundError(InventoryError):
    """Raised when a requested record doesn't exist"""

    status_code = 404

    def __init__(self, record_type: str, record_id: int):
        message = f"{record_type} with id {record_id} not found"
        details = {"record_type": record_type, "record_id": record_id}
        super().__init__(message, details)


class InsufficientStockError(InventoryError):
    """Raised when there isn't eough stock for an operation"""

    status_code = 400

    def __init__(
        self, product_id: int, location_id: int, requested: int, available: int
    ):
        message = f"Insufficient stock for product {product_id}"
        details = {
            "product_id": product_id,
            "requested": requested,
            "available": available,
            "location_id": location_id,
        }
        super().__init__(message, details)
