import pytest
from transfer_funds import transfer_funds


# =============================================================================
# Tests for Function 4: Transfer Funds
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestTransferFunds:
    def test_fails_to_calculate_interest_when_rate_is_negative(self):
           with pytest.raises(ValueError):
               transfer_funds({"name": "Alice", "balance": 100000}, {"name": "KJK", "balance": 100000}, -1000)

    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(ValueError):
                transfer_funds({"name": "Alice", "balance": 50001}, {"name": "KJK", "balance": 100000}, 50001)

    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(TypeError):
                transfer_funds({"name": "Alice", "balance": 100000}, {"name": "KJK", "balance": 100000}, "Hello")

    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(ValueError):
                transfer_funds({"name": "Alice", "balance": 50001}, {"name": "KJK", "balance": 100000}, 50001)

    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(TypeError):
                transfer_funds({"name": "Alice", "balance": 100000}, {"name": "KJK", "balance": 100000}, -1000)