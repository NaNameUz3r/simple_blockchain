from blockchain.blockchain import Blockchain


def test_proof():
    b = Blockchain()
    print(b.proof_of_work(9392929392939239923992))
