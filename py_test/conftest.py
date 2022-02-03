import pytest

@pytest.fixture(scope="session")
def test_zhu():
    return 'zhangxiaoming'



@pytest.fixture(params=[(4,2),(3,5)])
def data(request):
    return request.param
