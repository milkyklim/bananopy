from decimal import Decimal

BASE_UNIT = "raw"
UNIT_NAMES = ["ban", "banano"]
UNITS_TO_RAW = {
    "raw": Decimal(1),
    "banoshi": Decimal(10 ** 27),
    "ban": Decimal(10 ** 29),
    "banano": Decimal(10 ** 29),
}


def convert(value, from_unit, to_unit):
    if isinstance(value, float):
        raise TypeError(
            (
                "Float values can lead to unexpected precision loss, please use",
                f"Decimal or string e.g. convert({value}, {from_unit}, {to_unit})",
            )
        )

    if from_unit not in UNITS_TO_RAW:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in UNITS_TO_RAW:
        raise ValueError(f"Unknown unit: {to_unit}")

    try:
        value = Decimal(value)
    except Exception:
        raise ValueError(f"Not a number: {value}")

    from_value_in_base = UNITS_TO_RAW[from_unit]
    to_value_in_base = UNITS_TO_RAW[to_unit]

    result = value * (from_value_in_base / to_value_in_base)

    return result
