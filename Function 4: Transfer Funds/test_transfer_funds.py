import pytest
from transfer_funds import transfer_funds


# =============================================================================
# Tests for Function 4: Transfer Funds
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestTransferFunds:

    def test_successfully_transfers_funds_without_fee(self):
        sender = {"name": "Alice", "balance": 1000}
        receiver = {"name": "Bob", "balance": 500}

        updated_sender, updated_receiver = transfer_funds(sender, receiver, 200)

        assert updated_sender["balance"] == 800
        assert updated_receiver["balance"] == 700

    def test_boundary_of_exactly_50000_charges_no_fee(self):
        sender = {"name": "Alice", "balance": 100000}
        receiver = {"name": "Bob", "balance": 0}

        updated_sender, updated_receiver = transfer_funds(sender, receiver, 50000)

        # No fee at exactly 50,000, since fee only applies when amount > 50000
        assert updated_sender["balance"] == 50000
        assert updated_receiver["balance"] == 50000

    def test_charges_fee_for_transfer_exceeding_50000(self):
        sender = {"name": "Alice", "balance": 100000}
        receiver = {"name": "Bob", "balance": 0}

        updated_sender, updated_receiver = transfer_funds(sender, receiver, 60000)

        fee = 60000 * 0.001  # 60.0
        assert updated_sender["balance"] == 100000 - 60000 - fee
        assert updated_receiver["balance"] == 60000  # receiver gets full amount, no fee

    def test_does_not_mutate_original_account_dictionaries(self):
        sender = {"name": "Alice", "balance": 1000}
        receiver = {"name": "Bob", "balance": 500}

        transfer_funds(sender, receiver, 200)

        # Original dicts should remain untouched
        assert sender["balance"] == 1000
        assert receiver["balance"] == 500

    def test_fails_when_sender_has_insufficient_funds(self):
        sender = {"name": "Alice", "balance": 100}
        receiver = {"name": "Bob", "balance": 0}

        with pytest.raises(ValueError, match="Insufficient funds"):
            transfer_funds(sender, receiver, 200)

    def test_fails_when_sender_has_insufficient_funds_including_fee(self):
        # Balance covers the transfer amount but not the fee on top
        sender = {"name": "Alice", "balance": 60000}
        receiver = {"name": "Bob", "balance": 0}

        with pytest.raises(ValueError, match="Insufficient funds"):
            transfer_funds(sender, receiver, 60000)  # needs 60000 + 60 fee = 60060

    def test_fails_when_amount_is_not_positive(self):
        sender = {"name": "Alice", "balance": 1000}
        receiver = {"name": "Bob", "balance": 500}

        with pytest.raises(ValueError, match="Transfer amount must be positive"):
            transfer_funds(sender, receiver, 0)