import pytest
from dojo import fizz_buzz_backwards


@pytest.mark.parametrize(
    "entrance expected".split(),
    (
        ([1, 2, "Fizz", 4, "Buzz", 6],  [3, 5]),
        ([1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"], [2, 3]),
        ([1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"], [2, 2]),
        (["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"], [1, 6]),
        (
            [
                1, 2, 3, 4, 5, 6, 'Fizz', 8, 9, 10, 'Buzz', 12, 13,
                'Fizz', 15, 16, 17, 18, 19, 20, 'Fizz', 'Buzz', 23,
                24, 25, 26, 27, 'Fizz', 29, 30, 31, 32, 'Buzz', 34,
                'Fizz', 36, 37, 38, 39, 40, 41, 'Fizz', 43, 'Buzz',
                45, 46, 47, 48, 'Fizz', 50, 51, 52, 53, 54, 'Buzz',
                'Fizz', 57, 58, 59, 60, 61, 62, 'Fizz', 64, 65, 'Buzz',
                67, 68, 69, 'Fizz', 71, 72, 73, 74, 75, 76,
                'FizzBuzz', 78, 79
            ],
            [7, 11]
        ),
    )
)
def test_fizz_buzz_backwards(entrance, expected):
    assert fizz_buzz_backwards(entrance) == expected
