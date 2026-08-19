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
        # Arrange
        current_balance = 100
        contribution = 0
        expected_balance = 100
        # Act
        new_balance = receive_contribution(current_balance, contribution)
        # Assert
        assert new_balance == expected_balance

    def test_successfully_adds_deposit_to_account_with_zero_balance(self):
        current_balance = 0
        contribution = 50

        with pytest.raises(ValueError, match="Contribution must be positive"):
            receive_contribution(current_balance, contribution)


    def test_fails_to_add_deposit_when_balance_is_negative(self):
        current_balance = -10
        contribution = 50

        with pytest.raises(ValueError, match="Balance cannot be negative"):
            receive_contribution(current_balance, contribution)
            pass

    def test_fails_to_add_deposit_when_contribution_is_zero(self):
        current_balance = 100
        contribution = 0

        with pytest.raises(ValueError, match="Contribution must be positive"):
            receive_contribution(current_balance, contribution)
            pass
        

    def test_fails_to_add_deposit_when_contribution_is_negative(self):
        current_balance = 100
        contribution = -50

        pass
