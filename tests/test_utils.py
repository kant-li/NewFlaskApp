"""
test utils functions
"""

from pytest import mark

from app.utils.utils import valid_email_address, generate_verification_code


@mark.utils
def test_valid_email_address() -> None:
    assert valid_email_address('test@email.com')
    assert valid_email_address('test_email.com') is False
    assert valid_email_address('test@.com') is False
    assert valid_email_address('@email.com') is False
    assert valid_email_address('test@email.') is False
    assert valid_email_address('test@') is False


@mark.utils
def test_generate_verification_code() -> None:
    assert len(generate_verification_code()) == 6
