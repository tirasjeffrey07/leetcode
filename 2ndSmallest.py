"""
Second largest element in an array

map(function,iterable) returns a sequence of values after applying the function on each value of iterable
have to convert it to list using list()

numbers=list(reversed(numbers)) faster than extended slicing
numbers[::-1] refer https://docs.python.org/release/2.3.5/whatsnew/section-slices.html for string slicing
also works

"""

n = int(input())
arr=map(int ,input().split())
numbers = list(arr)

numbers.sort()

biggest = numbers[n-1]

if n < 2:
    print("Invalid")

numbers.reverse()

for i in range(n):
    if numbers[i] < biggest:
        print(numbers[i])
        break

