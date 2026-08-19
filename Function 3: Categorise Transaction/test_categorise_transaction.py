import pytest
from categorise_transaction import categorise_transaction


# =============================================================================
# Tests for Function 3: Categorise Transaction
#
# Read the docstring, then write your own tests. Aim for 6 test cases.
# =============================================================================

class TestCategoriseTransaction:

    def test_returns_zero_for_zero_amount(self):
        result = categorise_transaction(0)
        assert result == "zero"

    def test_returns_credit_for_ordinary_positive_amount(self):
        result = categorise_transaction(500)
        assert result == "credit"

    def test_returns_debit_for_ordinary_negative_amount(self):
        result = categorise_transaction(-500)
        assert result == "debit"

    def test_boundary_of_exactly_10000_is_credit_not_large(self):
        result = categorise_transaction(10000)
        assert result == "credit"

    def test_boundary_of_exactly_negative_10000_is_debit_not_large(self):
        result = categorise_transaction(-10000)
        assert result == "debit"

    def test_returns_large_credit_when_amount_exceeds_10000(self):
        result = categorise_transaction(10000.01)
        assert result == "large credit"

    def test_returns_large_debit_when_amount_exceeds_negative_10000(self):
        result = categorise_transaction(-10000.01)
        assert result == "large debit"

    def test_raises_type_error_for_non_numeric_amount(self):
        with pytest.raises(TypeError, match="Amount must be a number"):
            categorise_transaction("500")