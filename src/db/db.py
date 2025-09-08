from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from src.config import DATABASE_URL
import logging
import time
import sys
from src.db.base import Base

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

from src.db.models.default import DefaultDatabase

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def wait_for_postgres(max_retries=30, retry_interval=2):
    logger.info("Aguardando PostgreSQL ficar disponível...")
    for i in range(max_retries):
        try:
            with engine.connect() as conn:
                logger.info("PostgreSQL está disponível!")
                return True
        except Exception as e:
            logger.warning(f"Tentativa {i+1}/{max_retries}: PostgreSQL não está disponível - {e}")
            time.sleep(retry_interval)
    logger.error("PostgreSQL não ficou disponível a tempo.")
    return False

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    if not wait_for_postgres():
        sys.exit(1)
    
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    logger.info(f"Tabelas existentes antes: {existing_tables}")
    
    logger.info("Criando tabelas...")
    
    logger.info(f"Modelos registrados: {Base.metadata.tables.keys()}")
    
    Base.metadata.create_all(engine)
    
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    logger.info(f"Tabelas criadas: {tables}")
    
    if tables:
        logger.info("Tabelas criadas com sucesso!")
        return True
    else:
        logger.error("Nenhuma tabela foi criada!")
        return False

if __name__ == "__main__":
    init_db()