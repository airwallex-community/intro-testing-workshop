def process_batch_transactions(
    opening_balance: float, transactions: list[dict]
) -> dict:
    """
    Apply a list of transactions to an opening balance and return a summary.

    Each transaction is a dict with "type" (either "credit" or "debit") and
    "amount" (a positive float). Transactions are applied in order: credits
    increase the balance, debits decrease it.

    Invalid transactions are silently skipped rather than raising an error.
    A transaction is considered invalid if its type is not "credit" or "debit",
    or its amount is zero or negative. A debit that would cause the balance
    to drop below zero is also skipped.

    Args:
        opening_balance: The starting balance. Must be >= 0.
        transactions: A list of transaction dicts,
            e.g. [{"type": "credit", "amount": 500.0}, ...].

    Returns:
        A summary dict containing:
          - "opening_balance": The original starting balance.
          - "closing_balance": The balance after all transactions.
          - "total_credits": Sum of all applied credit amounts.
          - "total_debits": Sum of all applied debit amounts.
          - "transactions_processed": Count of successfully applied transactions.
          - "transactions_skipped": Count of skipped transactions.

    Raises:
        ValueError: If the opening balance is negative.
    """
    if opening_balance < 0:
        raise ValueError("Opening balance cannot be negative")

    balance = opening_balance
    total_credits = 0.0
    total_debits = 0.0
    processed = 0
    skipped = 0

    for txn in transactions:
        txn_type = txn.get("type")
        amount = txn.get("amount", 0)

        if txn_type not in ("credit", "debit") or amount <= 0:
            skipped += 1
            continue

        if txn_type == "credit":
            balance += amount
            total_credits += amount
            processed += 1
        elif txn_type == "debit":
            if balance - amount < 0:
                skipped += 1
                continue
            balance -= amount
            total_debits += amount
            processed += 1

    return {
        "opening_balance": opening_balance,
        "closing_balance": balance,
        "total_credits": total_credits,
        "total_debits": total_debits,
        "transactions_processed": processed,
        "transactions_skipped": skipped,
    }
