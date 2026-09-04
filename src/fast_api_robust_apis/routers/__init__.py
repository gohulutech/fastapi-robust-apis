from fast_api_robust_apis.routers.products import router as products_router
from fast_api_robust_apis.routers.locations import router as locations_router
from fast_api_robust_apis.routers.inventory import router as inventory_router

routers = [products_router, locations_router, inventory_router]
