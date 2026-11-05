
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# FUEL BILL TESTS

def test_invalid_fuel_grade():
    with pytest.raises(ValueError):
        fuel_bill("kerosene", 20, "silver")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_litres_within_coverage():
    assert fuel_bill("regular", 8, "silver") == 0


def test_gold_loyalty_discount():
    assert fuel_bill("regular", 50, "gold") == 35 * 95


def test_diesel_fuel_rate():
    assert fuel_bill("diesel", 30, "silver") == 10 * 90


def test_large_fuel_purchase():
    assert fuel_bill("premium", 60, "silver") == 45 * 99


# PUMP ALLOWED TESTS

def test_fleet_request_allowed():
    assert pump_allowed(150, 3, True) is True


def test_non_fleet_request_exceeds_limit():
    assert pump_allowed(70, 1, False) is False


def test_non_fleet_request_allowed():
    assert pump_allowed(30, 1, False) is True


# SESSION STATUS TESTS

def test_card_payment_night_active():
    assert session_status(100, True, True) == "active"


def test_cash_payment_day_warning():
    assert session_status(20, False, False) == "warning"


def test_session_timed_out():
    assert session_status(10, False, False) == "timed_out"

