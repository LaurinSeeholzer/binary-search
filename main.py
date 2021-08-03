#binary search algorithm implemented in python
#made by Laurin Seeholzer in august 2021


#first we need to sort the list
#we could just use List.sort()
#but because we aren't noobs, we sort it by ourselves
#therfor we use radix msd or better known as quicksort algorithm

#quick sort / Radix MSD algorithm
#O(l*n)
def radix_msd_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    base = max(unsorted_list).bit_length() - 1
    return sort(unsorted_list, 0, len(unsorted_list) - 1, base, unsorted_list)

def sort(l, i, j, base, unsorted_list):
    m, n = i, j
    while m <= n:
        if unsorted_list[m] >> base & 1 == 0:
            m += 1
            continue
        else:
            if unsorted_list[n] >> base & 1 == 0:
                unsorted_list[n], unsorted_list[m] = unsorted_list[m], unsorted_list[n]
                m += 1
            n -= 1
    if base > 0 and i < j:
        sort(l, i, m-1, base-1, unsorted_list)
        sort(l, m, j, base-1, unsorted_list)
    return unsorted_list

#for searching a number in our given list we use binary search
#we use binary search bacause it's simple and often used
def binary_search(List, number_to_find):
	low = 0
	high = len(List) - 1
	while low <= high:
		middle = low + (high - low) // 2

		if List[middle] == number_to_find:
			return middle
		elif List[middle] < number_to_find:
			low = middle + 1
		else:
			high = middle - 1
	return -1



#create unique list
import random
List = []
for i in range(100):
    new_int = random.randint(0, 99)
    if new_int in List:
        pass
    else:
        List.append(new_int)

number_to_search = 0


#asking for number to search
print(List)
def ask():
    number_to_search = int(input("number to search:  "))
    if type(number_to_search) is int:
        return number_to_search
    else:
        print(type(number_to_search))
        print("thats not an integer")
        ask()
number_to_search = ask()


#actually sorting the list
print("sorting list...")
sorted_List = radix_msd_sort(List)
print("list sorted")
print(sorted_List)


#searching given value in sorted list
result = binary_search(sorted_List, number_to_search)
if result == -1:
    print(str(number_to_search) + " was not in the list")
else:
    print("the number " + str(number_to_search) + " was found at index " + str(result))
