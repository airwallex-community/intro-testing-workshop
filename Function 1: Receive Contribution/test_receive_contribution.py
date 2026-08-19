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
        current_balance = 10
        contribution = 5
        expected_balance = 15

        new balance = receive_contribution(current_balance, contribution)
        assert new_balance == expected_balance
        pass    

    def test_successfully_adds_deposit_to_account_with_zero_balance(self):
        # Arrange 
        current_balance = 0
        contribution = 1 
        expected_balance = 1 

        # Act 
        new_balance - receive_contribution(current_balance, contribution)

        # Assert 
        assert new_balance == expected_balance
        pass

    def test_fails_to_add_deposit_when_balance_is_negative(self):
        current balance = -1 
        contribution = 1 
        with pytest.raises(ValueError, match="Current balance cannot be negative"):
            receive_contribution(current_balance, contribution)
        pass

    def test_fails_to_add_deposit_when_contribution_is_zero(self):
        if contribution == 0: 
            pytest.praise(Error, match="Contribution cannot be zero")
        pass

    def test_fails_to_add_deposit_when_contribution_is_negative(self):
        if contribution < 0: 
            pytest.raise(Error, match="Contribution cannot be negative")
        pass
