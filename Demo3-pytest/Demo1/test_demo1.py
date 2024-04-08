import pytest
@pytest.fixture
def fruit_bowl():
    print("in before  fixture fruit_bowl")
    return ["apple", "banana"]

def test_fruit_salad1(fruit_bowl):
    print("in test_fruit_salad")
    print(fruit_bowl)
    assert "mango" in fruit_bowl , "The given fruit is not available in the fruit list"
    print("end test_fruit_salad")