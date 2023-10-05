from pydantic import BaseModel
from datetime import datetime


class SubmitTransaction(BaseModel):
    sender: str
    recipient: str
    amount: int


class TransactionResponse(BaseModel):
    block_id: int
    sender: str
    recipient: str
    amount: int
    timestamp: datetime
