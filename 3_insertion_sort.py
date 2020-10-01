l = [8, 2, 5, 4, 1, 3]

print(l)
# Implement an insertion sort algorithm
def insertion_sort(list_to_sort):
    # separate the first element and think of it as sorted
    # let us say its the first item in the list

    # for all other items(on the right on the first index)
    # ranged based starting at index 1
    for i in range(1, len(list_to_sort)):
        # put the current number in a temp var (temp)
        temp = list_to_sort[i]

        # keep track of current index as j
        j = i
        # keep looking left until we find where temp number belongs
        # while j is greater than zero (we are not past the start of the indces)
        # and our temp var is less than the number left of j
        while j > 0 and temp < list_to_sort[j - 1]:
            # as we look left, shift items to the right as we iterate
            list_to_sort[j] = list_to_sort[j - 1]
            # decrement j
            j -= 1

        # when left is smaller than temp, or we are at zero, put item in that spot
        list_to_sort[j] = temp

    # return list back to caller
    return list_to_sort

# lets try it
insertion_sort(l)

print(l)