import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg="Hello"
    print('tschuss!!!!!!!!!')
    assert msg=="Hi", "Testcase Failed: User Input is not equal to Hi"

@pytest.mark.smoke
def test_secondCreditCard():
    a,b=4,6
    assert a+2==6, "Testcase Failed: Addition do not match"
