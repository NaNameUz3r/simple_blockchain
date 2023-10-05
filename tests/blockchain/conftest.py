import pytest
from blockchain.blockchain import Blockchain


@pytest.fixture
def sample_blockchain():
    blockchain = Blockchain()
    blockchain.new_transaction("sender1", "recipient1", 10)
    last_proof = 12345
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_block(proof, blockchain.hash(blockchain.last_block))
    return blockchain
