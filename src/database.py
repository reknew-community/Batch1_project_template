from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings
import warnings

# -----------------------------
# Settings from .env
# -----------------------------
class Settings(BaseSettings):
    DATABASE_URL: str
    AUTO_CREATE_TABLES: bool = False  # keep False to avoid touching DB

    class Config:
        env_file = ".env"

settings = Settings()

# -----------------------------
# SQLAlchemy engine
# -----------------------------
connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# -----------------------------
# Dependency for FastAPI
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Auto-create tables safely
# -----------------------------
if settings.AUTO_CREATE_TABLES:
    try:
        print("Auto-creating tables (Vendor only)...")

        # Only create Vendor table automatically to avoid breaking relationships
        from src.models.vendor import Vendor
        Vendor.metadata.create_all(bind=engine)

        print("Vendor table created successfully.")

    except Exception as e:
        warnings.warn(f"Error auto-creating Vendor table: {e}")

# -----------------------------
# Optional: metadata reference for all models
# -----------------------------
# This is safe to import for type hinting or reference without touching DB
try:
    from src.models.roles import Role
    from src.models.user import User
    from src.models.customer import Customer
    # Vendor already imported above
except ImportError as e:
    warnings.warn(f"Model import warning: {e}")