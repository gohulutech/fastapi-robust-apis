from sqlalchemy.orm import Session

from fast_api_robust_apis.db.session import Base, engine
from fast_api_robust_apis.db.models import product, location, inventory


def init_db() -> None:
    """Initialize the database by creating all tables."""
    # Create tables
    Base.metadata.create_all(bind=engine)
