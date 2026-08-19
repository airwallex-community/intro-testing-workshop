import pytest
from calculate_interest import calculate_interest


# =============================================================================
# Tests for Function 2: Calculate Interest
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestCalculateInterest:
    def test_successfully_calculate_interest_with_all_successful_parametres(self):
        result = calculate_interest(50, 85, 2)
        assert result == 85.0
       
    def test_successfully_adds_calculate_interest_with_zero_balance(self):
        result = calculate_interest(0, 85, 2)
        assert result == 0.0

    def test_fails_to_calculate_interest_balance_is_negative(self):
        with pytest.raises(ValueError):
            calculate_interest(-10, 2, 3)

    def test_fails_to_calculate_interest_when_years_is_zero(self):
        pass

    def test_fails_to_add_deposit_when_contribution_is_negative(self):
        pass

    #balance: Must be >= 0
    # rate: Must be between 0 and 100 inclusive
    # years: Must be > 0

    # balance， rate， years