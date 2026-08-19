import pytest
from categorise_transaction import categorise_transaction

# =============================================================================
# Tests for Function 3: Categorise Transaction
#
# Read the docstring, then write your own tests. Aim for 6 test cases.
# =============================================================================

class TestCategoriseTransaction:
    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(TypeError):
                  categorise_transaction("Hello")
    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(TypeError):
                   categorise_transaction(True)

    def test_successfully_adds_calculate_interest_with_zero_balance(self):
        result = categorise_transaction(0)
        assert result == "zero"

    def test_successfully_adds_calculate_interest_with_zero_balance(self):
        result = categorise_transaction(200)
        assert result == "credit"

    def test_successfully_adds_calculate_interest_with_zero_balance(self):
        result = categorise_transaction(10001)
        assert result == "large credit"

    def test_successfully_adds_calculate_interest_with_zero_balance(self):
        result = categorise_transaction(-10001)
        assert result == "large debit"