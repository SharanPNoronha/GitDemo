# Any pytest file should start with test_ or end with _test
#In pytest testing standard, code must be written in Function
# pytest method names should start with test
#method names should hae sense
# -k stands for method names execution, -s logs in output,  -v stands for more info metadata
# You can run specific file with py.test <filename>
import pytest


def test_firstProgram(setup):
    print("Hello Sharan Noronhaaaa")

@pytest.mark.xfail   #this will run this testcase, but wont report it
def test_SecondGreetCreditCard():
    print("Sonnen sheint")
    print('tschuss!!!!!!!!!')
    print('tschuss!!!!!!!!!')
    print('tschuss!!!!!!!!!')
    print('tschuss!!!!!!!!!')

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1]) # this will run 3 times ( 1 with chrome, 1 with firefox, and then IE)

