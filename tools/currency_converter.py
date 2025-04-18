def currency_converter(amount: float, from_currency: str, to_currency: str) -> str:
    # Very basic, fixed-rate mock conversion
    rates = {
        ("USD", "INR"): 83.2,
        ("EUR", "INR"): 89.5,
        ("USD", "EUR"): 0.91,
    }

    key = (from_currency.upper(), to_currency.upper())
    if key not in rates:
        return f"❌ Conversion from {from_currency} to {to_currency} not supported."

    converted = amount * rates[key]
    return f"💱 {amount} {from_currency.upper()} ≈ {converted:.2f} {to_currency.upper()}"
