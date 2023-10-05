from pydantic import BaseModel
from blockchain.blockchain import Block


class ChainResponse(BaseModel):
    blockchain: list[Block]
    length: int
