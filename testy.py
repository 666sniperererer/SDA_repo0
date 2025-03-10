# Create an empty dictionary
'''
phonebook = {}

# Add two items
phonebook["John"] = [111,11,1,111]
phonebook["Jack"] = 222222222

print(phonebook)
print(phonebook["Jack"])
print(phonebook["John"])

# Definition of the finished dictionary
phonebook2 = {
    "John": 111111111,
    "Jack": 222222222
}

index_phonebook = 3
print(phonebook["John"][index_phonebook])
'''
import bisect
from os import remove

#import numpy as np
#print(np.random.randint(2,200))

'''
print([1, 2].extend([3, 4]))

s = {3, 4, 1, 1}
print(max(s))
print(s)
'''

'''
def print_longest_string(list_of_strings):
    longest_string = ""

    for item in list_of_strings:
        if len(item) > len(longest_string):
            longest_string = item

    print(longest_string)


strings = ["a", "asdasd", "asd", "asdasdasdad"]
print_longest_string(strings)
'''
'''
def input_birth_number():
    birth_number = ""
    char = ""
    allowed_chars = ["0","1","2","3","4","5","6","7","8","9","/"]
    print("Zadávej rodné číslo po jednom znaku, včetně lomítka."
          "\nZadáním @ potvrdíš, že je RČ zadáno celé.")
    while char != "@":
        char = input("Zadej znak: ")
        if char in allowed_chars:
            birth_number += str(char)
            print(f"Je zadáno: {birth_number}")
        elif char != "@":
            print(f"Zadání {char} není povoleno.")
    return birth_number

def convert_birth_number(birth_number):
    return int(birth_number.replace('/', ''))

def check_birth_number(birth_number):
    if birth_number % 11 == 0:
        print(f"Úspěch! {birth_number} je beze zbytku dělitelné 11ti.")
    else:
        print("RČ nemá správný formát, opakuj celé zadání.")
        birth_number = input_birth_number()
        birth_number = convert_birth_number(birth_number)
        check_birth_number(birth_number)
    return birth_number

check_birth_number(convert_birth_number(input_birth_number()))
'''
'''
# TODO: list_sum(numbers), která rekurzivně sčíta čísla v seznamu
def list_sum(numbers) -> int:
    if len(numbers) == 1:
        return numbers[0]
    numbers[0] += numbers.pop()
    return list_sum(numbers)

print(list_sum([5,3,6,9])) # -> 23

# TODO: count_char(string, character), která rekurzivně spočíta „character" v řetězci
def count_char(text: str, character: str) -> int:
    if not text:
        return 0
    #return (1 if text[0] == character else 0) + count_char(text[1:], character) #validní v pořádku!
    return (text[0] == character) + count_char(text[1:], character)

print(count_char("hello", "l")) # -> 2
print(count_char("Algoritmy jsou super zabava", "a"))  # -> 3

# TODO: fib(n), která rekurzivně vypočíta n-té Fibonacciho číslo
# fibo -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,.....
def fibo_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

import time

print(fibo_recursive(1)) # -> 1
print(fibo_recursive(4)) # -> 3
print(fibo_recursive(5)) # -> 5



#print(fibo_recursive(51))



def fibo_recursive_dynamic(n, memo={0:0, 1:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo_recursive_dynamic(n - 1, memo) + fibo_recursive_dynamic(n - 2, memo)
        return memo[n]


print(fibo_recursive_dynamic(1)) # -> 1
print(fibo_recursive_dynamic(4)) # -> 3
print(fibo_recursive_dynamic(5)) # -> 5

time_start = time.time()

print(fibo_recursive_dynamic(1000)) # -> 5

print(f"Fibo_recursive_dynamic 1000 běželo celkem {time.time() - time_start} sekund")


'''
'''
#rekurze - proveřit string, jestli je palindrom
def check_palindrom_recursive(text: str) -> bool:
    if len(text) == 0 or len(text) == 1:
        return True
    else:
        char1 = text[0]
        text = text[1:]

        char2 = text[-1]
        text = text[:-1]

        if char1 == char2:
            return check_palindrom_recursive(text)
        else:
            return False

print(check_palindrom_recursive("abba"))

import re
sum = 0
pattern = 'back'
if re.match(pattern, 'backup.txt'):
    sum +=1

if re.match(pattern, 'text.back'):
    sum +=2

if re.search(pattern, 'backup.txt'):
    sum +=4

if re.search(pattern, 'text.back'):
    sum +=8

print(sum)

param = (i*i for i in range(5))
print(type(param))

# TODO: Pouzit nejaou funkci knihovny bisect
# bisect.insort, bisect.bisect (nebo verze left right)
# Spoj a serad dva seznamy do jednoho

def merge_two_lists(list1, list2):
    list3 = []
    for number in list1:
        bisect.insort(list3, number)
    for number in list2:
        bisect.insort(list3, number)
    return list3

print(merge_two_lists([2, 8, 3], [87, 75, 6]))  # -> [2, 3, 6, 8, 75, 87]

def bubble_sort_optimal(my_array):
    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):  # TODO: define range
            if my_array[j] > my_array[j+1]:  # TODO define condition
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True #TODO: define value
        if not swapped:
            break  # TODO: define operation

    return my_array


print("Sorted array:", bubble_sort_optimal([5, 1, 7, 3, 9, 12, 11]))

def insert_sort_optimal(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array[i]
        for j in range(i-1,-1,-1): #TODO: define range
            if current_value < my_array[j]: #TODO: define condition
                my_array[j+1] = my_array[j] # TODO: define operation
                insert_index = j
            else:
                break
        my_array[insert_index] = current_value
    return my_array

print("Sorted array:", insert_sort_optimal([64, 34, 25, 12, 22, 11, 90, 5]))

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
'''
'''
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
       if left[i] <= right[j]:
           result.append(left[i])
           i += 1
       else:
          result.append(right[j])
          j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    print(mid)
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

print("Sorted array:", mergeSort([64, 34, 25, 12, 22, 11, 90, 5, 6]))
'''
