Summation
Write a program that finds the summation of every number between 1 and num. The number will always be a positive integer 
greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
tests
test.describe('Summation')
test.it('Should return the correct total')
test.assert_equals(summation(1), 1)
test.assert_equals(summation(8), 36)

others solution:
def summation(num):
    return (1+num) * num / 2
or
def summation(num):
    return sum(range(1,num+1))
or
def summation(num):
    if num > 1:
       return num + summation(num - 1)
    return 1
