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

