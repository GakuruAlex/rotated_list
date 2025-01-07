import pytest
from rotated_list_binary_sol import rotated_list_binary_sol


#One rotation with positive integers
@pytest.mark.parametrize("numbers, rotation", [
    ([14, 0, 4, 5, 6, 8, 10], 1),
    ([8, 1, 3, 5, 7], 1),
    ([24, 3, 5, 6, 8, 20, 21, 22, 23], 1)
])
def test_rotated_list_binary_sol_with_one_rotation(numbers, rotation):
    assert rotated_list_binary_sol(numbers) == rotation


#More than one rotation with one number
@pytest.mark.parametrize("numbers, rotation", [
    ([14, 15, 16, 2, 5, 7, 10], 3),
    ([25, 28, 30, 33, 35, 42, 11, 14, 16, 20, 22], 6),
    ([25, 28, 30, 33, 20, 22], 4)
])
def test_rotated_list_binary_sol_with_more_than_one_rotation(numbers, rotation):
    assert rotated_list_binary_sol(numbers) == rotation

#Empty list
def test_rotated_list_binary_sol_with_an_empty_list():
    assert rotated_list_binary_sol([]) == -1

#One rotation with negative integers
@pytest.mark.parametrize("numbers, rotation",[
    ([-2, -12, -10, -8, -5, -4], 1),
    ([-10, -14, -13, -12, -11], 1),
    ([-20, -50, -45, -40, -35, -30, -25], 1)
])
def test_rotated_list_binary_sol_with_list_rotation_and_negative_ints(numbers, rotation):
    assert rotated_list_binary_sol(numbers) == rotation


#Test for list with n rotations or 0 rotations
@pytest.mark.parametrize("numbers, rotation", [
    ([2, 3, 4, 5, 6, 7], 0),
    ([2], 0),
    ([-10, -8, -7, -5, -3, -1], 0),
    ([-4], 0)
])
def test_rotated_list_binary_sol_with_n_rotaions(numbers, rotation):
    assert rotated_list_binary_sol(numbers) == rotation

#Test with a list of both positive and negative numbers
@pytest.mark.parametrize("numbers, rotation", [
    ([10, 12, 14, -10, -8, -5, 0], 3),
    ([20, -20, -10, -5, 0], 1),
    ([-20, -15, -10, 0, 5, 15, 20], 0),
    ([15, 20, -20, -15, -10, -5, 0, 5], 2)
])
def test_rotated_list_binary_sol_with_both_positive_and_negative_integers(numbers, rotation):
    assert rotated_list_binary_sol(numbers) == rotation

#Test with a rotated list that has repeated numbers
@pytest.mark.parametrize("numbers, rotation", [
    ([10, 12, 12, 14, 14, -10, -10, -5, 0, 0], 5),
    ([20, -20, -10, -5, 0, 20, 20], 1),
])
def test_rotated_list_binary_sol_with_list_of_repeated_numbers(numbers, rotation):
    assert rotated_list_binary_sol(numbers) == rotation