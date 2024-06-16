from sqlalchemy.orm import Session
from . import models, schemas

def get_leader(db: Session, leader_id: int):
    return db.query(models.Leader).filter(models.Leader.id == leader_id).first()

def get_leaders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Leader).offset(skip).limit(limit).all()

def create_leader(db: Session, leader: schemas.LeaderCreate):
    db_leader = models.Leader(**leader.model_dump())
    db.add(db_leader)
    db.commit()
    db.refresh(db_leader)
    return db_leader

def update_leader(db: Session, leader_id: int, leader: schemas.LeaderCreate):
    db_leader = db.query(models.Leader).filter(models.Leader.id == leader_id).first()
    if db_leader is None:
        return None
    for key, value in leader.model_dump().items():
        setattr(db_leader, key, value)
        db.commit()
        db.refresh(db_leader)
        return db_leader

def delete_leader(db: Session, leader_id: int):
    db_leader = db.query(models.Leader).filter(models.Leader.id == leader_id).first()
    if db_leader is None:
        return None
    db.delete(db_leader)
    db.commit()
    return db_leader

def get_leader_power(db: Session, leader_power_id: int):
    return db.query(models.LeaderPower).filter(models.LeaderPower.id == leader_power_id).first()

def create_leader_power(db: Session, leader_power: schemas.LeaderPowerCreate):
    db_leader_power = models.LeaderPower(**leader_power.dict())
    db.add(db_leader_power)
    db.commit()
    db.refresh(db_leader_power)
    return db_leader_power

def update_leader_power(db: Session, leader_power_id: int, leader_power: schemas.LeaderPowerCreate):
    db_leader_power = db.query(models.LeaderPower).filter(models.LeaderPower.id == leader_power_id).first()
    if db_leader_power is None:
        return None
    for key, value in leader_power.model_dump().items():
        setattr(db_leader_power, key, value)
    db.commit()
    db.refresh(db_leader_power)
    return db_leader_power

def delete_leader_power(db: Session, leader_power_id: int):
    db_leader_power = db.query(models.LeaderPower).filter(models.LeaderPower.id == leader_power_id).first()
    if db_leader_power is None:
        return None
    db.delete(db_leader_power)
    db.commit()
    return db_leader_power

