from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Any, NewType
import json
import hashlib


NodeMined = NewType("NodeMined", bool)


@dataclass
class Block:
    index: int
    timestamp: str
    transactions: list[Any]
    proof_of_work: int
    previous_hash: str


@dataclass
class Transaction:
    sender: str | NodeMined
    recipient: str
    amount: int


class Blockchain(object):
    def __init__(self):
        self.chain: list[Block] = []
        self.current_transactions: list[Transaction] = []
        self.nodes: set = set()

        self.new_block(previous_block_hash="1", proof_of_work=100)

    @property
    def last_block(self) -> Block:
        """
        Last block getter from chain
        """
        if len(self.chain) <= 0:
            raise Exception("Blockchain is empty")
        return self.chain[-1]

    def new_block(
        self,
        proof_of_work: int,
        previous_block_hash: str | None = None,
    ) -> Block:
        """
        Create a new block and append it in the blockchain.

        __pre-conditions__:
            - Block is mined.

        __post-conditions__:
            - New valid block added in the blockchain.

        """

        new_block = Block(
            index=len(self.chain) + 1,
            timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            transactions=self.current_transactions,
            proof_of_work=proof_of_work,
            previous_hash=previous_block_hash or self.hash(self.chain[-1]),
        )

        self.current_transactions = []
        self.chain.append(new_block)
        return new_block

    def new_transaction(
        self,
        sender: str | NodeMined,
        recipient: str,
        amount: int,
    ) -> int:
        """
        Appends a new transaction which is goes into the next
        mined Block.

        __pre-conditions__:

        __post-conditions__:
            - Returned the index of the block that will hold created transaction
        """

        self.current_transactions.append(
            Transaction(
                sender=sender,
                recipient=recipient,
                amount=amount,
            )
        )

        return self.last_block.index + 1

    @staticmethod
    def hash(block: Block) -> str:
        """
        Hashes a block by SHA-256.

        __post-conditions__:
            - returned a valid hash of provided Block
        """

        # Sort block for consistent hash
        sorted_block = json.dumps(obj=asdict(block), sort_keys=True).encode()
        return hashlib.sha256(string=sorted_block).hexdigest()

    def proof_of_work(self, last_proof: Any):
        """
        Drastically simple proof of work algorithm:
        __pre-condition__:
            - authentic last proof given
        __post-condition__:
            - returned an integer reflecting the number of guess,
            resulting as hash-string started with four zeroes.
        """

        proof_count = 0
        while (
            self.is_valid_proof(
                last_proof=last_proof,
                proof=proof_count,
            )
            is False
        ):
            proof_count += 1

        return proof_count

    @classmethod
    def is_valid_proof(
        cls,
        last_proof: int,
        proof: int,
    ):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
