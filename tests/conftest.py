import tomllib
import logging
from pathlib import Path

import pytest

configpath = Path("./tstconfig.toml")

@pytest.fixture
def read_config():
    with open(configpath, "rb") as conf:
        return tomllib.load(conf)
    

@pytest.fixture
def logger(request, read_config):
    log_path = read_config['paths']['log']
    func_name = request.function.__name__
 

@pytest.fixture
def get_urls(read_config):
    return read_config['Recipe']['urls']