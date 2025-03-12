def bubble_sort_optimal(my_array):
    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break

    return my_array

print("Sorted array:", bubble_sort_optimal([5, 1, 7, 3, 9, 12, 11]))


def insert_sort(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array[i]
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                my_array[j+1] = my_array[j]
                insert_index = j
            else:
                break
        my_array[insert_index] = current_value
    return my_array

print("Sorted array:", insert_sort([64, 34, 25, 12, 22, 11, 90, 5]))



def selection_sort_optimal(my_array):
    n = len(my_array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

    return my_array


print("Sorted array:", selection_sort_optimal([64, 34, 25, 12, 22, 11, 90, 5]))



def merge(left, right):
    result = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:  # TODO define condition
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

def mergeSort(arr):
    if len(arr) <= 1: #TODO: end condition for recursion
        return arr

    mid = len(arr) // 2 #TODO: find middle
    leftHalf = arr[:mid] #TODO: define left half
    rightHalf = arr[mid:] #TODO: define right half

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Merge sorted array:", sortedArr)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


my_array4 = [64, 34, 25, 12, 22, 11, 90, 5]
print("Quick sorted array:", quicksort(my_array4), my_array4)

