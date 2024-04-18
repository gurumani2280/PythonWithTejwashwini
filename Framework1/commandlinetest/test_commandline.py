import pytest


@pytest.mark.usefixtures("clsetup")
class TestCL :
    @pytest.mark.cl
    def test_cl(self):
        print("running test cl")