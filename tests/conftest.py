import tomllib
import logging
from pathlib import Path, PurePath

import pytest

conftest_path = Path(__file__)
configpath = Path.joinpath(conftest_path.parent, "tstconfig.toml")

with open(configpath, "rb") as conf:
    urls = tomllib.load(conf)["Recipe"]["urls"]


@pytest.fixture
def read_config():
    with open(configpath, "rb") as conf:
        return tomllib.load(conf)


@pytest.fixture
def logger(request, read_config):
    log_path = read_config["paths"]["log"]
    func_name = request.function.__name__


def pytest_generate_tests(metafunc):
    if "url" in metafunc.fixturenames:
        metafunc.parametrize("url", urls)
