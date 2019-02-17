def binary_search(list_of_numbers, number):
    lens = len(list_of_numbers)
    left, rite = 0 , lens - 1
    while left <= rite:
        mid = (left + rite) // 2
        print(mid, left, rite)
        if number > list_of_numbers[mid]:
            left = mid + 1
        elif number < list_of_numbers[mid]:
            rite = mid - 1
        else:
            return mid
    raise ValueError("{} not in list or invalid search parameters.".format(number))

#print(binary_search([1, 3, 4, 6, 8, 9, 11], 11))