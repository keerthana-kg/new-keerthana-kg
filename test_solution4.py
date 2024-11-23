from solution4 import *

# Easy Tests
def test_union_sets_easy():
    assert union_sets({1, 2}, {2, 3}) == {1, 2, 3}

def test_add_element_easy():
    assert add_element({1, 2}, 3) == {1, 2, 3}

def test_is_subset_easy():
    assert is_subset({1}, {1, 2, 3}) == True

# Moderate Tests
def test_intersection_sets_moderate():
    assert intersection_sets({1, 2, 3}, {2, 3, 4}) == {2, 3}

def test_symmetric_difference_moderate():
    assert symmetric_difference({1, 2, 3}, {3, 4, 5}) == {1, 2, 4, 5}

def test_remove_element_moderate():
    assert remove_element({1, 2, 3}, 2) == {1, 3}

# Tough Tests
def test_difference_sets_tough():
    assert difference_sets(set(range(1, 100)), set(range(50, 150))) == set(range(1, 50))

def test_is_disjoint_tough():
    assert is_disjoint({1, 2}, {3, 4}) == True

def test_clear_set_tough():
    assert clear_set({1, 2, 3}) == set()
