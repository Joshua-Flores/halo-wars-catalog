from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from . database import SessionLocal, engine

# Create database tabels
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/leaders/", response_model=schemas.Leader)
def create_leader(leader: schemas.LeaderCreate, db: Session = Depends(get_db)):
    return crud.create_leader(db=db, leader=leader)

@app.get("/leaders/", response_model=List[schemas.Leader])
def read_leaders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    leaders = crud.get_leaders(db, skip=skip, limit=limit)
    return leaders

@app.get("/leaders/{leader_id}", response_model=schemas.Leader)
def read_leader(leader_id: int, db: Session = Depends(get_db)):
    db_leader = crud.get_leader(db, leader_id=leader_id)
    if db_leader is None:
        raise HTTPException(status_code=404, detail="Leader not found")
    return db_leader

@app.put("/leaders/{leader_id}", response_model=schemas.Leader)
def update_leader(leader_id: int, leader: schemas.LeaderCreate, db: Session = Depends(get_db)):
    db_leader = crud.update_leader(db, leader_id=leader_id, leader=leader)
    if db_leader is None:
        raise HTTPException(status_code=404, detail="Leader not found")
    return db_leader

@app.delete("/leaders/{leader_id}", response_model=schemas.Leader)
def delete_leader(leader_id: int, db: Session = Depends(get_db)):
    db_leader = crud.delete_leader(db, leader_id=leader_id)
    if db_leader is None:
        raise HTTPException(status_code=404, detail="Leader not found")
    return db_leader

@app.post("/leader_powers/", response_model=schemas.LeaderPower)
def create_leader_power(leader_power: schemas.LeaderPowerCreate, db: Session = Depends(get_db)):
    return crud.create_leader_power(db=db, leader_power=leader_power)

@app.get("/leader_powers/{leader_power_id}", response_model=schemas.LeaderPower)
def read_leader_power(leader_power_id: int, db: Session = Depends(get_db)):
    db_leader_power = crud.get_leader_power(db, leader_power_id=leader_power_id)
    if db_leader_power is None:
        raise HTTPException(status_code=404, detail="Leader Power not found")
    return db_leader_power

@app.put("/leader_powers/{leader_power_id}", response_model=schemas.LeaderPower)
def update_leader_power(leader_power_id: int, leader_power: schemas.LeaderPowerCreate, db: Session = Depends(get_db)):
    db_leader_power = crud.update_leader_power(db, leader_power_id=leader_power_id, leader_power=leader_power)
    if db_leader_power is None:
        raise HTTPException(status_code=404, detail="Leader Power not found")
    return db_leader_power

@app.delete("/leader_powers/{leader_power_id}", response_model=schemas.LeaderPower)
def delete_leader_power(leader_power_id: int, db: Session = Depends(get_db)):
    db_leader_power = crud.delete_leader_power(db, leader_power_id=leader_power_id)
    if db_leader_power is None:
        raise HTTPException(status_code=404, detail="Leader Power not found")
    return db_leader_power