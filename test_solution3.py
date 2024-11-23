from solution3 import *

# Easy Tests
def test_find_max_easy():
    assert find_max([1, 2, 3]) == 3

def test_list_sum_easy():
    assert list_sum([1, 2, 3]) == 6

def test_append_element_easy():
    assert append_element([1, 2], 3) == [1, 2, 3]

# Moderate Tests
def test_average_moderate():
    assert average([1, 2, 3, 4]) == 2.5

def test_remove_element_moderate():
    assert remove_element([1, 2, 3], 2) == [1, 3]

def test_reverse_list_moderate():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]

# Tough Tests
def test_sort_list_tough():
    assert sort_list([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_count_occurrences_tough():
    assert count_occurrences([1, 2, 2, 3, 2], 2) == 3

def test_find_index_tough():
    assert find_index([10, 20, 30, 40], 30) == 2
