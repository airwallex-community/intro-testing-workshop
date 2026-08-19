import pytest
from receive_contribution import receive_contribution


# =============================================================================
# Tests for Function 1: Receive Contribution
#
# This first set of tests is laid out for you as an example.
# Read the docstring in receive_contribution.py, then fill in each test body.
# =============================================================================

class TestReceiveContribution:

    # current_balance must be >= 0
    # Contribution > 0
    # current_balance + contribution > 0
    # 1. current_balance, 2. contribution


    def test_successfully_adds_deposit_to_account_with_existing_balance(self):
        result = receive_contribution(100, 50)
        assert result == 150

    def test_successfully_adds_deposit_to_account_with_zero_balance(self):
        result = receive_contribution(0, 50)
        assert result == 50

    def test_fails_to_add_deposit_when_balance_is_negative(self):
        with pytest.raises(ValueError, match="Current balance cannot be negative"):
            receive_contribution(-10, 50)

    def test_fails_to_add_deposit_when_contribution_is_zero(self):
        with pytest.raises(ValueError):
            receive_contribution(50, 0)

    def test_fails_to_add_deposit_when_contribution_is_negative(self):
        with pytest.raises(ValueError):
            receive_contribution(50, -10)
