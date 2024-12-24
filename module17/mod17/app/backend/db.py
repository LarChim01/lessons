from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine


engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

