import pytest
import bananopy.banano as ban
from bananopy.conversion import convert
from bananopy import __version__

from decimal import Decimal


def test_version():
    assert __version__ == "0.3.3"


@pytest.mark.parametrize(
    "amount,expected",
    [
        # strings
        (str(1 * 10 ** 29), Decimal("1")),
        (str(1 * 10 ** 27), Decimal("0.01")),
        ("1", Decimal("1e-29")),
        # integers
        (1919 * 10 ** 29, Decimal("1919")),
        (1, Decimal("1e-29")),
        # decimals
        (Decimal("19"), Decimal("19e-29")),
        (Decimal("19e29"), Decimal("19")),
    ],
)
def test_ban_from_raw(amount, expected):
    assert ban.ban_from_raw(amount) == expected


@pytest.mark.parametrize(
    "amount,expected",
    [
        # strings
        ("1", Decimal(1 * 10 ** 29)),
        ("0.01", Decimal(1 * 10 ** 27)),
        ("1e-29", Decimal("1")),
        # integers
        (1919, Decimal(1919 * 10 ** 29)),
        # decimals
        (Decimal("19e-29"), Decimal("19")),
        (Decimal("19"), Decimal("19e29"),),
    ],
)
def test_ban_to_raw(amount, expected):
    assert ban.ban_to_raw(amount) == expected


@pytest.mark.parametrize(
    "amount,expected",
    [
        # strings
        ("19", Decimal("1900")),
        ("0.19", Decimal("19")),
        ("2.4", Decimal("240")),
        ("1000000", Decimal("100000000")),
        ("0.0042", Decimal("0.42")),
        # integers
        (19, Decimal("1900")),
        # decimals
        (Decimal("1000000"), Decimal("100000000")),
        (Decimal("0.0042"), Decimal("0.42")),
    ],
)
def test_ban_to_banoshi(amount, expected):
    assert ban.ban_to_banoshi(amount) == expected


@pytest.mark.parametrize(
    "amount,expected",
    [
        # strings
        ("1900", Decimal("19")),
        ("19", Decimal("0.19")),
        ("240", Decimal("2.4")),
        ("100000000", Decimal("1000000")),
        ("0.42", Decimal("0.0042")),
        # integers
        (1900, Decimal("19")),
        # decimals
        (Decimal("100000000"), Decimal("1000000")),
        (Decimal("0.42"), Decimal("0.0042")),
    ],
)
def test_ban_from_banoshi(amount, expected):
    assert ban.ban_from_banoshi(amount) == expected


@pytest.mark.parametrize(
    "value,from_unit,to_unit,ex",
    [
        (19.0, "ban", "banoshi", TypeError),
        (19, "ban", "baboshi", ValueError),
        (19, "nano", "ban", ValueError),
        ("Hey!", "ban", "banoshi", ValueError),
    ],
)
def test_convert(value, from_unit, to_unit, ex):
    with pytest.raises(ex):
        convert(value, from_unit, to_unit)
