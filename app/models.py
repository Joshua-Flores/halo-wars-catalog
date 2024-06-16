from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Leader(Base):
    __tablename__ = "leaders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    faction = Column(String)
    background = Column(String)

    leader_powers = relationship("LeaderPower", back_populates="leader")

class LeaderPower(Base):
    __tablename__ = "leader_powers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    power_tier = Column(Integer)
    cooldown_time = Column(Integer)
    leader_id = Column(Integer, ForeignKey('leaders.id'))

    leader = relationship("Leader", back_populates="leader_powers")


