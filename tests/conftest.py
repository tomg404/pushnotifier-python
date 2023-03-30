def pytest_addoption(parser):
    parser.addoption("--user", action="store")
    parser.addoption("--password", action="store")
    parser.addoption("--token", action="store")
    parser.addoption("--package", action="store")
