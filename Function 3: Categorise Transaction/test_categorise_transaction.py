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
                calculate_interest("Hello")

    def test_fails_to_calculate_interest_when_rate_is_negative(self):
            with pytest.raises(TypeError):
                calculate_interest(True)