import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_CONNECTOR = os.getenv('DB_CONNECTOR')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD= os.getenv('DB_PASSWORD')
DB_DRIVER= os.getenv('DB_DRIVER')

# DATABASE__URL = f'''{DB_CONNECTOR}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}''' # Gestor de postgres

DATABASE__URL = (
    f"{DB_CONNECTOR}://{DB_USERNAME}:"
    f"{DB_PASSWORD}@{DB_HOST}/"
    f"{DB_DATABASE}?driver={DB_DRIVER}"
)

engine = create_engine(DATABASE__URL, fast_executemany=True)

# Configuración de la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

