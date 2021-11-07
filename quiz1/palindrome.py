def palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome
    :param value: A string
    :return: A boolean
    """

    j=len(value)-1
    for i in range(0,j,1):
        if value[i] != value[j]:
            return False

        j -= 1
        return True

#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 % python3 -m unittest quiz1.test_palim
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#OK
#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 %


