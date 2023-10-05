from fastapi.routing import APIRouter
from starlette import status
from uuid import uuid4
from blockchain.blockchain import Blockchain, NodeMined
from api.core.schema.blockchain import ChainResponse
from api.core.schema.transaction import SubmitTransaction, TransactionResponse
from api.core.schema.mine import MineResponse
from datetime import datetime

router = APIRouter()


node_id = str(uuid4()).replace("-", "")
blockchain = Blockchain()


@router.get(
    path="/mine",
    status_code=status.HTTP_200_OK,
    response_model=
)
def mine_block():
    last_block = blockchain.last_block
    last_proof = last_block.proof_of_work
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_transaction(
        sender=NodeMined(True),
        recipient=node_id,
        amount=1,
    )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    return MineResponse(message="New block forged",
                        index=block.index,
                        transactions=block.transactions,
                        proof_of_work=block.proof_of_work,
                        previous_hash=block.previous_hash,
                        )


@router.post(
    path="/transactions/new",
    status_code=status.HTTP_200_OK,
    response_model=TransactionResponse,
)
def new_transaction(payload: SubmitTransaction):
    index = blockchain.new_transaction(
        sender=payload.sender,
        recipient=payload.recipient,
        amount=payload.amount,
    )

    return TransactionResponse(
        block_id=index,
        sender=payload.sender,
        recipient=payload.recipient,
        amount=payload.amount,
        timestamp=datetime.utcnow(),
    )


@router.get(
    path="/chain",
    response_model=ChainResponse,
    status_code=status.HTTP_200_OK,
)
def get_whole_chain():
    return ChainResponse(blockchain=blockchain.chain, length=len(blockchain.chain))
