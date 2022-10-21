def binarySearch(item, list):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        #mid = len(list)//2
        if item == list[mid]:
            return mid
        elif item < list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


result = binarySearch(8, [1, 2, 3, 4, 5, 6, 7, 7.2, 7.4, 7.5, 8, 9])
print(f'Item is at index - {result}')

"""
start time = 13:06
finished = 16:15
Issue = the script is stuck suggesting it is either in infinite loop or there is an error that is witholding the script to compile
Traceback error=
File "/Users/mawhinneym/Projects/Python/BinarySearch.py", line 19, in <module>
    result = binarySearch(8, [1, 2, 3, 4, 5, 6, 7, 7.2, 7.5, 8, 9])
  File "/Users/mawhinneym/Projects/Python/BinarySearch.py", line 8, in binarySearch
    if item == list[mid]:
The longest time i spent on this problem was to run it similar to recusion where the mid can be found by simply by len(list)//2. however since recusion & looping are 2 different concepts, going through the list elements is different when recursing and when looping.
"""
