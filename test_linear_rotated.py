import pytest
from linear_rotated import rotated_list_linear_sol

@pytest.mark.parametrize("numbers, rotation", [
    ([14, 0, 4, 5, 6, 8, 10], 1),
    ([8, 1, 3, 5, 7], 1),
    ([24, 3, 5, 6, 8, 20, 21, 22, 23], 1)
])
def test_rotated_list_linear_sol(numbers, rotation):
    assert rotated_list_linear_sol(numbers) == rotation