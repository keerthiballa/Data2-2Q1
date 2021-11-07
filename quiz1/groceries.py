def checkout(cash: float, list: dict) -> float:
    """
    build a function that sums up the value of the grocery list and subtracts that
    from the cash passed into the function.
    return the "change" from the cash minus the total groceries value.
    """
    total=float()
    for key,value in list.items():
        total = total + value
    return (cash-total)

#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 % python3 -m unittest quiz1.test_groceries
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.000s
#
#OK
#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 %
