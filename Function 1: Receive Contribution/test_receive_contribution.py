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
        
        pass    

    def test_successfully_adds_deposit_to_account_with_zero_balance(self):

        pass

    def test_fails_to_add_deposit_when_balance_is_negative(self):
        if current_balance < 0: 
            raise ValueError("Current balance cannot be negative")
        pass

    def test_fails_to_add_deposit_when_contribution_is_zero(self):
        if contribution == 0: 
            raise ValueError("Contribution cannot be zero")
        pass

    def test_fails_to_add_deposit_when_contribution_is_negative(self):
        if contribution < 0: 
            raise ValueError("Contribution cannot be negative")
        pass
