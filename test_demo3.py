#Fixture concept demo
import pytest
'''  #written this fixture in the conftest file
@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print('after yield: I will be executed last')
'''

def test_fixtureDemo(setup):
    print("I will be execute steps in fixtureDemo method")

def test_fixtureDemo1(setup):
    print("I will be execute steps in fixtureDemo1 method")

def test_fixtureDemo2(setup):
    print("I will be execute steps in fixtureDemo2 method")

def test_fixtureDemo3(setup):
    print("I will be execute steps in fixtureDemo3 method")
# to tell this function that it depends upon the fixture, so pass the fixture method name as parameters.
# so first the fixture method will be executed and then this method.
# so its kind of prerequisite. # In selenium, we use this fixtures for initial setup such as opening the browser, get website,
    #and so on.
#only when you pass fixture as an argument to the methods, only then it will be tied up to the fixture.
