def transfer_funds(
    sender: dict, receiver: dict, amount: float
) -> tuple[dict, dict]:
    """
    Transfer funds between two accounts.

    Each account is a dictionary with keys "name" (str) and "balance" (float).
    The full transfer amount is credited to the receiver. For transfers
    exceeding 50,000, a 0.1% fee is charged to the sender on top of the
    transfer amount — the sender's balance is reduced by the transfer amount
    plus the fee, while the receiver only receives the transfer amount.

    The original account dictionaries are not modified; new dictionaries are
    returned with updated balances.

    Args:
        sender: The sending account, e.g. {"name": "Alice", "balance": 100000}.
        receiver: The receiving account.
        amount: The amount to transfer. Must be > 0.

    Returns:
        A tuple of (updated_sender, updated_receiver) dictionaries.

    Raises:
        ValueError: If amount is not positive, or if the sender has
            insufficient funds to cover the transfer (including any fee).
    """
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")

    fee = amount * 0.001 if amount > 50000 else 0.0
    total_deducted = amount + fee

    if sender["balance"] < total_deducted:
        raise ValueError("Insufficient funds")

    updated_sender = {**sender, "balance": sender["balance"] - total_deducted}
    updated_receiver = {**receiver, "balance": receiver["balance"] + amount}
    return updated_sender, updated_receiver
