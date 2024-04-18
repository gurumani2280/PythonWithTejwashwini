# content of test_sample.py
import pytest


@pytest.mark.usefixtures("cmdopt")
class TestSample :
    @pytest.mark.sample
    def test_answer(cmdopt):
        print("*******************",cmdopt)
        print(cmdopt)
        if cmdopt == "Edge".lower():
            print("Edge")
        elif cmdopt == "Firefox".lower():
            print("Firefox")
        else:
            print("Chrome")
        assert 0  # to see what was printed