import re
import math
def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers
def encoding(str,lenka):
    a = [i for i in str]
    a = get_unique_numbers(a)
    string = ""
    lenk = round(math.log(lenka, 2))
    coded = []
    for i in range(len(a)):
        n =bin(i).strip("0b")
        if len(n)< lenk:
            n = "0" *(lenk-len(n)) +n
        coded.append(n)
    for el in str:
        ind = a.index(el)
        string += coded[ind]
    return string


str = input()
print(encoding(str, len(str)))