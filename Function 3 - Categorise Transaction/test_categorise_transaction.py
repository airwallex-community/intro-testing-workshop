import pytest
from categorise_transaction import categorise_transaction


# =============================================================================
# Tests for Function 3: Categorise Transaction
#
# Read the docstring, then write your own tests. Aim for 6 test cases.
# =============================================================================

class TestCategoriseTransaction:

    @pytest.mark.parametrize(
        ("amount", "expected"),
        [
            (0, "zero"),                    # Zero amount
            (1, "credit"),                  # Normal positive amount
            (-1, "debit"),                  # Normal negative amount
            (10_000, "credit"),             # Positive boundary is not large
            (-10_000, "debit"),             # Negative boundary is not large
            (10_000.01, "large credit"),    # Just above positive boundary
            (-10_000.01, "large debit"),    # Just below negative boundary
        ],
    )
    def test_categorises_amount_at_each_boundary(self, amount, expected):
        """Return the correct category for normal amounts and boundaries."""
        assert categorise_transaction(amount) == expected

    @pytest.mark.parametrize("amount", ["100", None, [], {}])
    def test_rejects_non_numeric_amount(self, amount):
        """Raise TypeError when the amount is not an integer or float."""
        with pytest.raises(TypeError):
            categorise_transaction(amount)

 # parameterisation to avoid repetition of similar tests, and to make it easy to add more test cases in the future.         