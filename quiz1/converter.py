def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.
    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    return round(meters*3.28084,2)


def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.
    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """
    return round(feet/3.28084,2)



#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 % python3 -m unittest quiz1.test_converter
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.000s

#OK
#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 %
#
