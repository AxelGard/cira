import cira


def test_checking_keys():
    """To check if keys are correct we need walid keys"""
    assert not cira.auth.check_keys()
