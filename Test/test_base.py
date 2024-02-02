import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:

    def tear_down_method(self,setup):
        self.driver.close()
