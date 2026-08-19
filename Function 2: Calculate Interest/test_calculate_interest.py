import pytest
from calculate_interest import calculate_interest


# =============================================================================
# Tests for Function 2: Calculate Interest
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# =============================================================================

class TestCalculateInterest:
    balance = 1000
    rate = 5
    years = 3

    interest = calculate_interest(balance, rate, years)
    assert interest == 150.0
    pass

