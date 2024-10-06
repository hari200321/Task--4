#1 What is the expected output of the following python code given below:
data = [10,501,22,37,100,999,87,351]
result = filter (lambda x: x>4,data)
print(list(result))
OUTPUT — [10, 501, 22, 37, 100, 999, 87, 351]

# 2 Write a Python code using Lambda function to check every element of a List
# is an Integer or string?
from functools import reduce

test_list = [[5,6,3],[“Gfg”, 3, “is”],[9, “best”, 4]]

print(“The original list : “ + str(test_list))

res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print(“The string instances : “ + str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print(“The string instances : “ + str(res1))

OUTPUT — The original list : [[5, 6, 3], [‘Gfg’, 3, ‘is’], [9, ‘best’, 4]] The string instances : [‘Gfg’, ‘is’, ‘best’] The string instances : [5, 6, 3, 3, 9, 4]
                                                                                                   

#3) Using a python Lambda function create a fibonacci series from 1 to 50 elements?

def fibonacci(count):
fib_list = [0, 1]

any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
range(2, count)))

return fib_list[:count]

print(fibonacci(50))

OUTPUT — [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]



#3) Using a python Lambda function create a fibonacci series from 1 to 50 elements?

def fibonacci(count):
fib_list = [0, 1]

any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
range(2, count)))

return fib_list[:count]

print(fibonacci(50))

OUTPUT — [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]


#4) Write a Python function to validate the Regular Expression for the following:-
# a) Email Address
#b) Mobile numbers of Bangaladesh
#c) Telephone numbers of USA
#d) 16 character Alpha-Numeric password composed of alphabets of Uppercase,Lowercase,Special Characters,Numbers.

