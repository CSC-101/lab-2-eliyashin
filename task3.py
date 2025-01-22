def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # This statement is evaluated in the second call
    else:
        return m

first = smallest(3,2)       # The value of first is 2
second = smallest(2, 2)      # The value of second is 2. This result is reasonable because it does not fall under the first condition.
print()


################################################################################################################
def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, a call to this function will evaluate this statement when a > b and a > c
    elif b > c:
        return b + c             # In general, a call to this function will evaluate this statement when b > c
    else:
        return 2 * c             # In general, a call to this function will evaluate this statement when the first and second condition are not true


answer1 = function2(3, 2, 1)     # The value of answer1 is 1
answer2 = function2(2, 3, 1)     # The value of answer2 is 4
answer3 = function2(2, 1, 3)     # The value of answer3 is 6
print()