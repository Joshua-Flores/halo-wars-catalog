from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class LeaderPowerBase(BaseModel):
    name: str
    description: str
    power_tier: int
    cooldown_time: int

class LeaderPowerCreate(LeaderPowerBase):
    leader_id: int

class LeaderPower(LeaderPowerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class LeaderBase(BaseModel):
    name: str
    faction: str
    background: Optional[str] = None

class LeaderCreate(LeaderBase):
    pass

class Leader(LeaderBase):
    id: int
    leader_powers: List[LeaderPower] = []
    model_config = ConfigDict(from_attributes=True)