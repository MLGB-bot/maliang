import decimal

def f2i(f, mode="ROUND_HALF_UP"):
    if isinstance(f, int):
        return f
    elif mode == "ROUND_HALF_UP":
        return int(decimal.Decimal(f).quantize(decimal.Decimal("0"), decimal.ROUND_HALF_UP))
    elif mode == "ROUND":
        return round(f)
    else:
        return int(f)