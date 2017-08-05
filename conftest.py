import pytest

def pytest_addoption(parser):
	parser.addoption("--apikey", action="store", default="", help="api_key")

# def pytest_generate_tests(metafunc):
# 	if 'apikey' in metafunc.fixturenames:
# 		metafunc.parametrize('apikey',metafunc.config.getoption('apikey'))

@pytest.fixture
def apikey(request):
    return request.config.getoption("--apikey")