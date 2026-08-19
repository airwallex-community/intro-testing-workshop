import pytest
from receive_contribution import receive_contribution


# =============================================================================
# Tests for Function 1: Receive Contribution
#
# This first set of tests is laid out for you as an example.
# Read the docstring in receive_contribution.py, then fill in each test body.
# =============================================================================

class TestReceiveContribution:

    def test_successfully_adds_deposit_to_account_with_existing_balance(self):
        assert receive_contribution(1_000, 250) == 1_250
        pass

    def test_successfully_adds_deposit_to_account_with_zero_balance(self):
        assert receive_contribution(0, 250) == 250
        pass

    def test_fails_to_add_deposit_when_balance_is_negative(self):
        with pytest.raises(ValueError):
            receive_contribution(-1, 250)
        pass

    def test_fails_to_add_deposit_when_contribution_is_zero(self):
        with pytest.raises(ValueError):
            receive_contribution(1_000, 0)
        pass

    def test_fails_to_add_deposit_when_contribution_is_negative(self):
        with pytest.raises(ValueError):
            receive_contribution(1_000, -1)
        pass