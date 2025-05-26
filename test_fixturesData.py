import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad): # when our fixture is returning or sending parameter. We must accept it by using Fixture method
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[2])