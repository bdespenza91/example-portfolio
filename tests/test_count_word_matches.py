import pytest
from count_word_matches import count_word_matches


# =========================================================
# Test Suite: count_word_matches
# =========================================================


# -------------------------------
# Exercise 1: Core Functionality
# -------------------------------
@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1),
        ("Dog dog DOG dOg", "dog", 4),
        ("Hello world", "world", 1),
        ("hello hello HELLO", "hello", 3),
        ("No matches here", "yes", 0),
        ("catcat cat catdog", "cat", 1),
        ("a a a", "a", 3),
    ],
    ids=[
        "basic_match",
        "case_insensitive",
        "single_match",
        "repeated_words",
        "no_match",
        "no_substring_match",
        "single_char_tokens",
    ]
)
def test_count_word_matches_core(text, target, expected):
    result = count_word_matches(text, target)
    assert result == expected


# -------------------------------
# Exercise 2: Edge Cases
# -------------------------------
@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("", "word", 0),
        ("hello world", "", 0),
        ("", "", 0),
        ("hello  world", "world", 1),
        (" cat ", "cat", 1),
        ("cat,dog cat", "cat", 1),
        ("x y z", "x", 1),
    ],
    ids=[
        "empty_text",
        "empty_target",
        "both_empty",
        "multiple_spaces",
        "leading_trailing_spaces",
        "punctuation_not_split",
        "single_char_word",
    ]
)
def test_count_word_matches_edge_cases(text, target, expected):
    result = count_word_matches(text, target)
    assert result == expected


# -------------------------------
# Exercise 3: Negative Testing
# -------------------------------
@pytest.mark.parametrize(
    "text, target",
    [
        (None, "word"),
        ("hello world", None),
        (123, "word"),
        ("hello world", 456),
        (["hello", "world"], "world"),
        ("hello world", ["world"]),
    ],
    ids=[
        "text_none",
        "target_none",
        "text_int",
        "target_int",
        "text_list",
        "target_list",
    ]
)
def test_count_word_matches_invalid_inputs(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)
