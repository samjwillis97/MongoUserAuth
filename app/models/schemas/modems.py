from pydantic import BaseModel
from typing import Optional
import datetime

class ModemBase(BaseModel):
    location: str
    purpose: str
    gateway_ip: str
    ddns: str
    serial: str
    phone_number: str
    card_number: str

class Modem(ModemBase):
    signal: Optional[int] = None
    temperature: Optional[int] = None
    timestamp: Optional[datetime.datetime] = None
    wan: Optional[str] = None
    ddns: Optional[str] = None
    serial: Optional[str] = None
    phone_number: Optional[str] = None
    card_number: Optional[str] = None