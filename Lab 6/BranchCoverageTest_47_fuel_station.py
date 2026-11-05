
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# FUEL BILL - BRANCH COVERAGE

def test_unknown_fuel_grade():
    with pytest.raises(ValueError):
        fuel_bill("kerosene", 20, "gold")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -1, "silver")


def test_regular_silver_covered():
    assert fuel_bill("regular", 10, "silver") == 0


def test_regular_gold_extra():
    assert fuel_bill("regular", 20, "gold") == 5 * 105


def test_gold_diesel_no_extra_coverage():
    assert fuel_bill("diesel", 25, "gold") == 5 * 90


def test_diesel_large_purchase_silver():
    assert fuel_bill("diesel", 60, "silver") == 40 * 84


def test_regular_large_purchase_gold():
    assert fuel_bill("regular", 60, "gold") == 45 * 95


def test_premium_small_extra():
    assert fuel_bill("premium", 20, "silver") == 5 * 105


# PUMP ALLOWED - BRANCH COVERAGE

def test_fleet_within_limit():
    assert pump_allowed(200, 5, True) is True


def test_fleet_exceeds_limit():
    assert pump_allowed(201, 5, True) is False


def test_non_fleet_exceeds_litres():
    assert pump_allowed(61, 1, False) is False


def test_non_fleet_multiple_containers():
    assert pump_allowed(50, 2, False) is False


def test_non_fleet_single_container():
    assert pump_allowed(50, 1, False) is True


# SESSION STATUS - BRANCH COVERAGE

def test_card_day_active():
    assert session_status(60, True, False) == "active"


def test_card_night_warning():
    assert session_status(75, True, True) == "warning"


def test_card_night_timed_out():
    assert session_status(44, True, True) == "timed_out"


def test_cash_night_active():
    assert session_status(60, False, True) == "active"


def test_cash_day_warning():
    assert session_status(20, False, False) == "warning"


def test_cash_day_timed_out():
    assert session_status(14, False, False) == "timed_out"

