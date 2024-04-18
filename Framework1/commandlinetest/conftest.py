import os

import pytest


@pytest.fixture(scope="class")
def clsetup(request):
    browser = os.environ.get("BROWSER","CHROME")
    print("Browser",browser)
    browser1 = os.environ.get("BROWSER ", "CHROME")
    print("Browser1",browser1)


def pytest_addoption(parser):
    parser.addoption(
        "--Browser", action="store", default="chrome", help="my option: Edge or firefox"
    )


@pytest.fixture(scope="class")
def cmdopt(request):
    print("==============",request.config.getoption("--Browser"))
    return request.config.getoption("--Browser")
