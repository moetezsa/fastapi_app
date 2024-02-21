import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm


database_url = "postgresql://postgres:password@postgres:5432/db"
engine = sql.create_engine(database_url)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative.declarative_base()
