#!/usr/bin/python3
"""
This module declares the city model
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from relationship_state import State, Base


class City(Base):
    """
    City class linking to 'cities' MySQL table
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey(State.id, ondelete="CASCADE"),
                      nullable=False)

    state = relationship('State', back_populates='cities')


State.cities = relationship("City", order_by=City.id, back_populates='state')
