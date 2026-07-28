def calculate_interest(balance: float, rate: float, years: int) -> float:
    """
    Calculate simple interest earned on a savings account.

    Uses the formula: interest = balance * (rate / 100) * years.
    The result is rounded to 2 decimal places.

    Args:
        balance: The account balance to earn interest on. Must be >= 0.
        rate: The annual interest rate as a percentage (e.g. 5.5 for 5.5%).
            Must be between 0 and 100 inclusive.
        years: The number of years to calculate interest for. Must be > 0.

    Returns:
        The interest earned, rounded to 2 decimal places.

    Raises:
        ValueError: If balance is negative, rate is outside 0-100, or years
            is not positive.
    """
    if balance < 0:
        raise ValueError("Balance cannot be negative")
    if rate < 0 or rate > 100:
        raise ValueError("Rate must be between 0 and 100")
    if years <= 0:
        raise ValueError("Years must be a positive integer")
    return round(balance * (rate / 100) * years, 2)
