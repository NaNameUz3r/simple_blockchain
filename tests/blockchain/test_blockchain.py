from blockchain.blockchain import Blockchain, Block
import pytest
from datetime import datetime


def test__new_transaction__should_appends_to_transactions_list(sample_blockchain):
    initial_length = len(sample_blockchain.current_transactions)
    sample_blockchain.new_transaction("sender2", "recipient2", 5)
    assert len(sample_blockchain.current_transactions) == initial_length + 1


def test__new_block__should_be_added_in_blockchain(sample_blockchain):
    initial_length = len(sample_blockchain.chain)
    last_proof = 12345
    proof = sample_blockchain.proof_of_work(last_proof)
    sample_blockchain.new_block(proof, sample_blockchain.hash(sample_blockchain.get_last_block))
    assert len(sample_blockchain.chain) == initial_length + 1


def test__get_last_block__should_return_block_instance(sample_blockchain):
    last_block = sample_blockchain.get_last_block
    assert isinstance(last_block, Block)


def test__proof_of_work__should_be_true_for_valid_last_proof(sample_blockchain):
    last_proof = 12345
    proof = sample_blockchain.proof_of_work(last_proof)
    assert sample_blockchain.is_valid_proof(last_proof, proof)


def test__hash(sample_blockchain):
    block = Block(index=1,
                  timestamp="12/24/2018, 04:59:31",
                  transactions=[],
                  proof_of_work=12345,
                  previous_hash='previous_hash')
    calculated_hash = sample_blockchain.hash(block)
    assert (
        calculated_hash
        == "1db98e1f69cc050fcd98bd209b0a3dbda97674148e93e60a070e166c13944b62"
    )
