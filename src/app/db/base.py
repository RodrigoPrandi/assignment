# Import all the model, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.model.vehicle import Vehicle  # noqa
from app.model.user import User  # noqa
