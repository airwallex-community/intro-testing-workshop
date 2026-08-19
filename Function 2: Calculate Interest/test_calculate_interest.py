import pytest
from calculate_interest import calculate_interest


# =============================================================================
# Tests for Function 2: Calculate Interest
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestCalculateInterest:

    def test_successfully_calculates_interest_for_typical_values(self):
        # 1000 * (5/100) * 2 = 100.0
        result = calculate_interest(1000, 5, 2)
        assert result == 100.0

    def test_returns_zero_when_balance_is_zero(self):
        result = calculate_interest(0, 5, 2)
        assert result == 0.0

    def test_successfully_calculates_interest_at_maximum_rate(self):
        # rate = 100 is the upper boundary and should be valid
        result = calculate_interest(1000, 100, 1)
        assert result == 1000.0

    def test_fails_when_balance_is_negative(self):
        with pytest.raises(ValueError, match="Balance cannot be negative"):
            calculate_interest(-100, 5, 2)

    def test_fails_when_rate_exceeds_maximum(self):
        with pytest.raises(ValueError, match="Rate must be between 0 and 100"):
            calculate_interest(1000, 101, 2)

    def test_fails_when_years_is_zero(self):
        with pytest.raises(ValueError, match="Years must be a positive integer"):
            calculate_interest(1000, 5, 0)