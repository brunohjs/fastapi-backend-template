import sqlalchemy.orm


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
