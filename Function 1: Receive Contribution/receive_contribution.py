def receive_contribution(current_balance: int, contribution: int) -> int:
    """
    Deposit a contribution into a bank account and return the updated balance.

    The current balance must be non-negative and the contribution must be
    strictly positive. A zero or negative contribution is not considered valid.

    Args:
        current_balance: The account's existing balance. Must be >= 0.
        contribution: The amount to deposit. Must be > 0.

    Returns:
        The new account balance after the deposit.

    Raises:
        ValueError: If the current balance is negative or the contribution
            is not positive.
    """
    if current_balance < 0:
        raise ValueError("Current balance cannot be negative")
    if contribution <= 0:
        raise ValueError("Contribution must be positive")
    return current_balance + contribution

    # current_balance must be >= 0
    # Contribution > 0
    # current_balance + contribution > 0
