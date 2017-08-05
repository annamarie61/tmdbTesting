import pytest

def pytest_addoption(parser):
	parser.addoption("--apikey", action="store", default="", help="api_key")

@pytest.fixture
def apikey(request):
    return request.config.getoption("--apikey")