from pydantic import BaseModel
from blockchain.blockchain import Transaction


class MineResponse(BaseModel):
    message: str
    index: int
    transactions: list[Transaction]
    proof_of_work: int
    previous_hash: str
