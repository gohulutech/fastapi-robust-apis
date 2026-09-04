from fastapi import FastAPI
from fast_api_robust_apis.routers import routers

app = FastAPI(
    title="Inventory Management API",
    description="API for managing inventory across multiple locations",
    version="1.0.0",
)

for router in routers:
    app.include_router(router)


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint to verify API is running"""
    return {"status": "online", "message": "Inventory Management API is running"}
