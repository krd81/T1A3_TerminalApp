import main

# This is the only test I was able to do as it was the only method that did
# not reply on any user inputs or other methods which themselves relied 
# on user input


# remainder_check function finds the modulus of the 2 numbers given as arguments
# If there is a remainder, it returns 1. If no remainder it returns 0
def test_remainder():
    assert main.remainder_check(33, 10) == 1


def test_remainder2():
    assert main.remainder_check(100, 10) == 0


