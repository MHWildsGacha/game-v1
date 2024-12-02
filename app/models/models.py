from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.types import JSON 
from app.core.database import Base


Base = declarative_base()

user_card_association = Table(
    'user_card', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('card_id', Integer, ForeignKey('cards.id'), primary_key=True)
)

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  
    rarity = Column(Integer, nullable=False)
    attributes = Column(JSON, nullable=True) 
    description = Column(String, nullable=False)

    owners = relationship('User', secondary=user_card_association, back_populates='cards')

    def __repr__(self):
        return f"<Card(name={self.name}, rarity={self.rarity})>"

    def __str__(self):
        return f"Card: {self.name}, Rarity: {self.rarity}"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tickets = Column(Integer, default=0)
    cards = relationship('Card', secondary=user_card_association, back_populates='owners')

    def __repr__(self):
        return f"<User(id={self.id}, tickets={self.tickets})>"

    def __str__(self):
        return f"User ID: {self.id}, Tickets: {self.tickets}"
