from source.fuzzy_machine import membership_funcs
import pytest

@pytest.mark.parametrize(
    argnames=["input_value", "expected"],
    argvalues=[
        [0, 1],
        [0.3, 0.5],
        [0.6, 0],
        [1, 0],
    ]
)
def test_short_membership_function(input_value, expected)->None:
    actual = membership_funcs.short(input_value)
    assert actual == expected
    
@pytest.mark.parametrize(
    argnames=["input_value", "expected"],
    argvalues=[
        [0, 0],
        [0.3, 0.5],
        [0.6, 1],
        [1, 0],
    ]
)
def test_medium_membership_function(input_value, expected)->None:
    actual = membership_funcs.medium(input_value)
    assert actual == expected

#return (1/0.4)*(x-0.6)
@pytest.mark.parametrize(
    argnames=["input_value", "expected"],
    argvalues=[
        [0, 0],
        [0.3, 0],
        [0.6, 0],
        [1, 1],
    ]
)
def test_long_membership_function(input_value, expected)->None:
    actual = membership_funcs.long(input_value)
    assert actual == expected