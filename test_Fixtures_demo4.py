import pytest

@pytest.mark.usefixtures('setup')# if we use this, fixture method will be automatically be applied to all the methods of this class
class TestExample:

    def test_fixtureDemo(self):
        print("I will be execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will be execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will be execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will be execute steps in fixtureDemo3 method")