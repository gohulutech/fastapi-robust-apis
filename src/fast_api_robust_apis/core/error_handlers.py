from fastapi import Request
from fastapi.responses import JSONResponse
from fast_api_robust_apis.core.exceptions import InventoryError


async def inventory_exception_handler(request: Request, exc: InventoryError):
    """Handler for our custom inventory exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": True, "message": exc.message, "details": exc.details},
    )
