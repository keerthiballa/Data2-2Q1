def fibonacci(n: int) -> int:
    first_num = 0
    sec_num = 1
    if n>=0:
        for i in range(1,n):
            third_num = first_num + sec_num
            first_num = sec_num
            sec_num = third_num
    return third_num

#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 % python3 -m unittest quiz1.test_fibonacci
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#OK
#(venv) (base) ballakeerthi@zipcodes-MacBook-Pro-3 Data2-2Q1 %
#