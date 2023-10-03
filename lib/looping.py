#!/usr/bin/env python3
import io
import sys

def happy_new_year():
    count = 10
    
    while count >= 1:
        print(count)
        count -= 1
    
    print("Happy New Year!")

happy_new_year()


def square_integers(numbers):
    squared_list = [x ** 2 for x in numbers]
    return squared_list

input_list = [1, 2, 3, 4, 5]
result = square_integers(input_list)
print(result)  



def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


def test_prints_1_to_100_fizzbuzz():
    '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    fizzbuzz()
    sys.stdout = sys.__stdout__
    answer = captured_out.getvalue()
    assert len(answer) != 0, "Nothing printed! Check your loop condition. Also, do you have print statements?"


test_prints_1_to_100_fizzbuzz()


