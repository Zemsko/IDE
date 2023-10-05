import numpy as np 

MIN_MAGIC_NUMBER = 1
MAX_MAGIC_NUMBER = 100

def binarySearch(array, x, lowIndex:int, highIndex:int):
    # stores number of attempts
    attempt = 0
    
    # input array must be sorted
    array.sort()
    
    # Repeat until the pointers lowIndex and highIndex meet each other
    while lowIndex <= highIndex:
        
        # calculate number of attempts
        attempt = attempt + 1
        
        # get the middle point of input array
        mid = lowIndex + (highIndex - lowIndex)//2

        if array[mid] == x:
            return (mid, attempt)
                
        elif array[mid] < x:
            lowIndex = mid + 1

        else:
            highIndex = mid - 1
 
    return (None, attempt)

# generate magic number
magic_number = np.random.randint(MIN_MAGIC_NUMBER, MAX_MAGIC_NUMBER + 1)

print(f'Компьютер загадал число \'{magic_number}\'')

# generate array of number variants
array = list(range(MIN_MAGIC_NUMBER, MAX_MAGIC_NUMBER + 1))

position, attempt = binarySearch(array, magic_number, 0, len(array)-1)

if position != None:
    found_x = array[position]
    print(f'Загаданное число \'{found_x}\' было угадано с {attempt} попытки')
else:
    print(f'К сожалению загаданное по условию число \'{magic_number}\' не удалось обнаружить в массиве вариантов')

