import pytest
from blockchain.blockchain import Blockchain


@pytest.fixture()
def blockchain():
    blockchain = Blockchain()

    return blockchain
