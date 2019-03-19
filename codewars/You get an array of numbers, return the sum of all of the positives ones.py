You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
tests:
Test.describe("positive_sum")

Test.it("works for some examples")
Test.assert_equals(positive_sum([1,2,3,4,5]),15)
Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

soln(list comprehension)
sum(i for i in a if i>0)

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

soln mine:
def positive_sum(arr):
    arr_sum = 0
    for i in arr:
        if i > 0:
            arr_sum += i
    return arr_sum