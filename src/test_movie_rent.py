import main


def test_add():
    assert main.add(5, 3) == 8


""" Not possible to test as it is inside if "__name__" == "__main__" statement
def test_username_check():
    main.username_check('ricky19@gmail.com')
    assert True
 """

# remainder_check function finds the modulus of the 2 numbers given as arguments
# If there is a remainder, it returns 1. If no remainder it returns 0
def test_remainder():
    assert main.remainder_check(33, 10) == 1


def test_remainder2():
    assert main.remainder_check(100, 10) == 0

# def test_password_check('WhvjdnWE'):
