from solution1 import *

# Easy Tests
def test_reverse_string_easy():
    assert reverse_string("hello") == "olleh"

def test_count_vowels_easy():
    assert count_vowels("hello") == 2

def test_to_uppercase_easy():
    assert to_uppercase("hello") == "HELLO"

# Moderate Tests
def test_is_palindrome_moderate():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_replace_substring_moderate():
    assert replace_substring("hello world", "world", "there") == "hello there"

def test_split_string_moderate():
    assert split_string("apple,banana,cherry", ",") == ["apple", "banana", "cherry"]

# Tough Tests
def test_join_strings_tough():
    assert join_strings(["apple", "banana", "cherry"], "-") == "apple-banana-cherry"

def test_find_substring_tough():
    assert find_substring("The quick brown fox", "quick") == 4

def test_capitalize_string_tough():
    assert capitalize_string("hello world") == "Hello world"
