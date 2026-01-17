from number import check_number

def test_check_number_even_not_prime():
    assert check_number(6) == ["The Number is even", "The Number is not prime"]


