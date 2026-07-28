_applied_transactions: dict[str, dict] = {}


def apply_transaction(
    idempotency_key: str, account_balance: float, amount: float
) -> dict:
    """
    Apply a transaction to an account balance using an idempotency key.

    If a transaction with the same idempotency key has already been applied,
    the original result is returned and the balance is not modified again.
    This guarantees that callers can safely retry the same request without
    the transaction being applied more than once.

    On first call for a given key, the amount is added to the account balance
    (positive for credits, negative for debits). The result is stored
    internally so that subsequent calls with the same key return the same
    result regardless of the arguments passed.

    Args:
        idempotency_key: A unique string identifier for this transaction.
            Must be non-empty.
        account_balance: The current account balance.
        amount: The transaction amount (positive to credit, negative to debit).
            Must not be zero.

    Returns:
        A dict with:
          - "idempotency_key": The key that was used.
          - "previous_balance": The balance before the transaction.
          - "new_balance": The balance after the transaction.
          - "amount": The transaction amount that was applied.

    Raises:
        ValueError: If the idempotency key is empty or the amount is zero.
    """
    if not idempotency_key:
        raise ValueError("Idempotency key must not be empty")
    if amount == 0:
        raise ValueError("Amount must not be zero")

    if idempotency_key in _applied_transactions:
        return _applied_transactions[idempotency_key]

    result = {
        "idempotency_key": idempotency_key,
        "previous_balance": account_balance,
        "new_balance": account_balance + amount,
        "amount": amount,
    }
    _applied_transactions[idempotency_key] = result
    return result


def reset_applied_transactions() -> None:
    """Clear all stored transactions. Intended for use in tests."""
    _applied_transactions.clear()
