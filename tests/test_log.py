from datetime import datetime
import cira


def is_valid_time_format(val: str, time_format: str) -> bool:
    """Checks if time format is the same as given"""
    try:
        datetime.strptime(val, time_format)
        return True
    except ValueError:
        return False


def test_logging():
    """simple test for checking logging format"""
    act = "buy"
    sym = "BTC/USD"
    qty = 1
    res = cira.log.format_log_action(act, sym, qty)
    assert isinstance(res[3], str), "time was not included"
    assert is_valid_time_format(
        res[3], "%Y-%m-%d %H:%M"
    ), "time dose not follow the correct time format"
