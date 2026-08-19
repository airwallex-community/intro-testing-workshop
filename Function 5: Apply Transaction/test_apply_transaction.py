import pytest
from apply_transaction import apply_transaction, reset_applied_transactions


# =============================================================================
# Tests for Function 5: Apply Transaction (Idempotency)
#
# Read the docstring, then write your own tests. Aim for 5-6 test cases.
# Hint: use reset_applied_transactions() in a setup method to isolate tests.
# =============================================================================

class TestApplyTransaction:

    def setup_method(self):
        # Ensure each test starts with a clean slate, since transactions
        # are stored in module-level state that persists across calls.
        reset_applied_transactions()

    def test_successfully_applies_a_credit_transaction(self):
        result = apply_transaction("txn-1", 1000, 200)

        assert result["idempotency_key"] == "txn-1"
        assert result["previous_balance"] == 1000
        assert result["new_balance"] == 1200
        assert result["amount"] == 200

    def test_successfully_applies_a_debit_transaction(self):
        result = apply_transaction("txn-2", 1000, -300)

        assert result["previous_balance"] == 1000
        assert result["new_balance"] == 700
        assert result["amount"] == -300

    def test_retrying_same_key_returns_original_result_without_reapplying(self):
        first_result = apply_transaction("txn-3", 1000, 200)
        # Second call with same key but different balance/amount args
        second_result = apply_transaction("txn-3", 9999, 9999)

        # Should return the ORIGINAL result, ignoring the new arguments
        assert second_result == first_result
        assert second_result["new_balance"] == 1200

    def test_different_keys_are_applied_independently(self):
        result_a = apply_transaction("txn-a", 1000, 100)
        result_b = apply_transaction("txn-b", 1000, 100)

        assert result_a["new_balance"] == 1100
        assert result_b["new_balance"] == 1100
        assert result_a["idempotency_key"] != result_b["idempotency_key"]

    def test_fails_when_idempotency_key_is_empty(self):
        with pytest.raises(ValueError, match="Idempotency key must not be empty"):
            apply_transaction("", 1000, 200)

    def test_fails_when_amount_is_zero(self):
        with pytest.raises(ValueError, match="Amount must not be zero"):
            apply_transaction("txn-4", 1000,0)