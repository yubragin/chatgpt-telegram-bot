from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load the Alembic configuration
alembic_cfg = Config("alembic.ini")

# Retrieve the database URL from the Alembic configuration
database_url = alembic_cfg.get_main_option("sqlalchemy.url")

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a session
session = SessionLocal()
