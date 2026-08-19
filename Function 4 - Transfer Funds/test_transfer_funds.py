import pytest
from transfer_funds import transfer_funds


# =============================================================================
# Tests for Function 4: Transfer Funds
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestTransferFunds:
    def test_transfers_funds_between_accounts(self):
        """Deduct the amount from the sender and credit it to the receiver."""
        sender = {"name": "A", "balance": 1000}
        receiver = {"name": "B", "balance": 200}

        updated_sender, updated_receiver = transfer_funds(sender, receiver, 300)

        assert updated_sender == {"name": "A", "balance": 700}
        assert updated_receiver == {"name": "B", "balance": 500}

    def test_allows_sender_to_transfer_entire_balance(self):
        """Allow a transfer when the sender has exactly enough money."""
        sender = {"name": "A", "balance": 1000}
        receiver = {"name": "B", "balance": 0}

        updated_sender, updated_receiver = transfer_funds(sender, receiver, 1000)

        assert updated_sender["balance"] == 0
        assert updated_receiver["balance"] == 1000

    def test_charges_fee_only_above_boundary(self):
        """Charge a 0.1% fee only when the amount exceeds 50,000."""
        sender = {"name": "A", "balance": 100_000}
        receiver = {"name": "B", "balance": 0}

        sender_at_boundary, receiver_at_boundary = transfer_funds(
            sender, receiver, 50_000
        )
        sender_above_boundary, receiver_above_boundary = transfer_funds(
            sender, receiver, 60_000
        )

        assert sender_at_boundary["balance"] == 50_000
        assert receiver_at_boundary["balance"] == 50_000
        assert sender_above_boundary["balance"] == 39_940
        assert receiver_above_boundary["balance"] == 60_000

    def test_does_not_modify_original_accounts(self):
        """Return new account dictionaries without changing the originals."""
        sender = {"name": "A", "balance": 1000}
        receiver = {"name": "B", "balance": 200}

        updated_sender, updated_receiver = transfer_funds(sender, receiver, 300)

        assert sender == {"name": "A", "balance": 1000}
        assert receiver == {"name": "B", "balance": 200}
        assert updated_sender is not sender
        assert updated_receiver is not receiver

    def test_rejects_non_positive_amount(self):
        """Reject zero and negative transfer amounts."""
        sender = {"name": "A", "balance": 1000}
        receiver = {"name": "B", "balance": 0}

        with pytest.raises(ValueError, match="Transfer amount must be positive"):
            transfer_funds(sender, receiver, 0)

        with pytest.raises(ValueError, match="Transfer amount must be positive"):
            transfer_funds(sender, receiver, -1)

    def test_rejects_insufficient_funds(self):
        """Reject a transfer when the sender cannot cover the amount and fee."""
        receiver = {"name": "B", "balance": 0}

        with pytest.raises(ValueError, match="Insufficient funds"):
            transfer_funds({"name": "A", "balance": 999}, receiver, 1000)

        with pytest.raises(ValueError, match="Insufficient funds"):
            transfer_funds({"name": "A", "balance": 50_001}, receiver, 50_001)