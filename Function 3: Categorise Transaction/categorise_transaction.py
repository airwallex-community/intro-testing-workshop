def categorise_transaction(amount) -> str:
    """
    Categorise a transaction amount into a human-readable label.

    Positive amounts are categorised as "credit", negative as "debit", and
    zero as "zero". Amounts exceeding 10,000 in either direction are
    prefixed with "large" (i.e. "large credit" or "large debit"). The
    boundary value of exactly 10,000 or -10,000 is NOT considered large.

    Args:
        amount: The transaction amount. Must be an int or float.

    Returns:
        One of: "zero", "credit", "debit", "large credit", "large debit".
git checkout -b my-branch
    Raises:
        TypeError: If amount is not a numeric type (int or float).
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    if amount == 0:
        return "zero"
    if amount > 10000:
        return "large credit"
    if amount < -10000:
        return "large debit"
    if amount > 0:
        return "credit"
    return "debit"
