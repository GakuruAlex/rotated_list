import pytest
from linear_rotated import rotated_list_linear_sol

#One rotation with positive numbers
@pytest.mark.parametrize("numbers, rotation", [
    ([14, 0, 4, 5, 6, 8, 10], 1),
    ([8, 1, 3, 5, 7], 1),
    ([24, 3, 5, 6, 8, 20, 21, 22, 23], 1)
])
def test_rotated_list_linear_sol_with_one_rotation(numbers, rotation):
    assert rotated_list_linear_sol(numbers) == rotation


#More than one rotation with one number
@pytest.mark.parametrize("numbers, rotation", [
    ([14, 15, 16, 2, 5, 7, 10], 3),
    ([25, 28, 30, 33, 35, 42, 11, 14, 16, 20, 22], 6),
    ([25, 28, 30, 33, 20, 22], 4)
])
def test_rotated_list_linear_sol_with_more_than_one_rotation(numbers, rotation):
    assert rotated_list_linear_sol(numbers) == rotation