import pytest
from calculate_interest import calculate_interest


# =============================================================================
# Tests for Function 2: Calculate Interest
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestCalculateInterest:
    def test_calculate_interest_with_valid_inputs(self):
        # Arrange
        balance = 1000
        rate = 5
        years = 2
        expected_interest = 100
        
        # Act
        interest = calculate_interest(balance, rate, years)
        
        # Assert
        assert interest == expected_interest
        pass
    def test_calculate_interest_with_zero_balance(self):
        balance = 1000
        rate = 0
        years = 2
        
        with pytest.raises(ValueError, match="Rate must be between 0 and 100"):
            calculate_interest(balance, rate, years)
        pass   

    def test_calculate_interest_with_negative_balance(self):
        balance = -100
        rate = 9
        years = 3

        with pytest.raises(ValueError, match="Balance cannot be negative"):
            calculate_interest(balance, rate, years)
        pass
    
