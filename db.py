from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Goal(Base):
    __tablename__ = 'goal'

    id = Column(Integer, primary_key=True)
    name = Column("name", String(255))
    type = Column("type", String(255))
    description = Column("description", String(255))

    def __init__(self, id, name, type, description):
        self.id = id
        self.name = name
        self.type = type
        self.description = description

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.type}, {self.description})"


engine = create_engine('sqlite:///GoalsDb.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

pay_debt = Goal(id=1, name="pay debt", type="financial", description="pay off my debts")
session.add(pay_debt)
session.commit()
