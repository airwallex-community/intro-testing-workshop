import pytest
from calculate_interest import calculate_interest


# =============================================================================
# Tests for Function 2: Calculate Interest
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestCalculateInterest:
    def test_calculates_simple_interest(self):
        """It should calculate interest using balance, rate, and years."""
        assert calculate_interest(1000, 5, 2) == 100.00

    def test_rounds_interest_to_two_decimal_places(self):
        """It should round the calculated interest to two decimal places."""
        assert calculate_interest(1234.56, 5.5, 3) == 203.70

    @pytest.mark.parametrize(
        ("balance", "rate", "expected"),
        [(0, 50, 0.00), (1000, 0, 0.00), (1000, 100, 1000.00)],
    )
    def test_accepts_balance_and_rate_boundaries(self, balance, rate, expected):
        """It should accept zero balance and rates from 0 to 100 inclusive."""
        assert calculate_interest(balance, rate, 1) == expected

    def test_rejects_negative_balance(self):
        """It should reject a balance below zero."""
        with pytest.raises(ValueError, match="Balance cannot be negative"):
            calculate_interest(-0.01, 5, 1)

    @pytest.mark.parametrize("rate", [-0.01, 100.01])
    def test_rejects_rate_outside_inclusive_range(self, rate):
        """It should reject rates below 0 or above 100."""
        with pytest.raises(ValueError, match="Rate must be between 0 and 100"):
            calculate_interest(1000, rate, 1)

    @pytest.mark.parametrize("years", [0, -1])
    def test_rejects_non_positive_years(self, years):
        """It should reject zero or negative years."""
        with pytest.raises(ValueError, match="Years must be a positive integer"):
            calculate_interest(1000, 5, years)