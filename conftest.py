import pytest

@pytest.fixture(scope="class")
def setup():
    print('I will be executing First')
    yield
    print('I will be executing Last')

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")#Assume that we are editing the profile page, and we haver to send Fname and Lname
    return ["Sharan","Noronha","Google.com"]  # we can send this data at runtime to the method that needs it

@pytest.fixture(params=[('Chrome','Sharan', 'Noronha'),('Firefox','Jackson'),('IE','Pearl')])
def crossBrowser(request):
    return request.param