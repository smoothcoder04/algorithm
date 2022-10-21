# Exercise -> 4.1

def sum(arr):
    if arr == []:
        return 0
    return (arr[0] + sum(arr[1:]))


total = sum([1, 2, 3, 4])
print(f"sum total = ", total)

"""
Learning : the idea of recursion is to divide your problem to smaller chuncks, just like binary sort. however, quick sort achieves that with the use of recursion. Effective recursion is calling the same function without using loops. 
Quick sort = recursion + reduce size of recursion elements without using loops
"""

# Exercise -> 4.3 - find the max number in a list


def countNum(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    maxList = countNum(list[1:])
    return list[0] if list[0] > maxList else maxList


res = countNum([3000, 6, 3008, 10007, 20, 100])
print(f'the highest number in the list is {res}')

"""
Learning & Brain map-
as sson as you are asked to find the max using recursion, make sure you keep the fist element out - line 22
use the list/array method to find the max or sum of the elements - line 24


Essentially you will need to runt he whole programe to start backtracing and find your result which is not efficient for larger lists or bigger sets of numbers.
"""


# Exercise -> 4.2 - Count the number of elements in a list

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


result2 = count([12, 13, 14, 15])
print(result2)

# Exercise 4.4 - find base case & recursive case for binary search - search a number in a list
# OPTION 1


def binarySearch(item, list, start, end=None):
    if end == None:
        end = len(list)-1
    mid = start+end//2
    if item == list[mid]:
        return mid
    elif item < list[mid]:
        return binarySearch(item, list, start, mid-1)
    return binarySearch(item, list, mid+1, end)


result3 = binarySearch(5, [3, 5, 9, 12, 15], 0, None)
print(f'the item is found!!!!!!!!!!!! It is hiding at index {result3}')


"""
Exception1 - maximum recursion depth exceeded while calling a Python object
Solution - make sure the mid calculation of mid is outside the if statement in line 55 as mid will differ for first case when you are passing the entire list and the consecutive times when you'll reduce the list

Exception 2- local variable 'mid' referenced before assignment
Solution- This was also related to how the last return call was made + mid calculation

Exception 3 - TypeError: binarySearch() got multiple values for argument 'start'
Solution- never pass positional argument after keyword argument. Example - foo(a==2,c=3,9). Here, a=2 and c=3 are keyword argument. The 3rd argument 9 is a positional argument. This can not be interpreted by the python as to which key holds what value. best is to not mix the calls in recusion and use positional values.
"""

# Exercise 4.4 - find base case & recursive case for binary search - search a number in a list
# OPTION 2


def binarySearch2(item, list):
    mid = len(list)//2
    if len(list) == 1:
        return mid if list[mid] == item else None
    if item == list[mid]:
        return mid
    elif item < list[mid]:
        return binarySearch2(item, list[:mid])
    else:
        return mid + binarySearch2(item, list[mid:])


result4 = binarySearch2(5, [2, 5, 10, 11, 12])
print(f'the item is found again!!!!!!!!!!!! It is hiding at index {result4}')

"""
Total time spent on this solution = 2.5hrs

Most time was invested in getting the right index value

Line 91 & 93 are very important - how we get rid of the rest if the list matters when using recusion.
If the target item is in the beginning of the list you don't need to recursively add mid.
However, if it is in the end of the list you have to recursively add mid or the resulting previous index. This is to keep track of the element once the List is spliced so that you can locate the element in spliced list.

Line number 85. the confusion was to use len(list)//2 or len(list)-1//2
the latter do not make sense as // is the floor division that rounds the result to the nearest whole number, hence -1 don't make sense.
"""
