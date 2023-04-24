import pytest
from src.core.driver import Driver


@pytest.fixture(scope='function')
def driver(request):
    driver = Driver(request)
    yield driver.driver_instance
    request.addfinalizer(driver.finalize_test)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
