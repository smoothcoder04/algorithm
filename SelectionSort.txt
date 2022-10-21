# go through array and select the smallest element
def findSmallest(arr):
    smallest_index = 0
    smallest_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(1, len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    print(newArr)


selectionSort([2, 5, 3, 7, 1, 8])
