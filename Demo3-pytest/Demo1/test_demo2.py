import pytest
@pytest.fixture
def fruit_bowl2():
    print("in before  fixture fruit_bowl")
    yield ["apple", "banana"]
    print("in after  fixture fruit_bowl")



def test_fruit_salad2(fruit_bowl2):
    print("in test_fruit_salad")
    print(fruit_bowl2)
    assert "apple" in fruit_bowl2
    print("end test_fruit_salad")
