# Print all present the element from the array.
def static_array(arr):
    for l in arr:
        print(l)


# Print any one element from the array by index as a position(1 to n) of element.
def static_array_get_element(arr, capacity, index):
    if 0 < index <= capacity:
        print(arr[index-1])


# Insert an element anywhere in array for data manipulation.
def static_array_insert(arr, index, element, capacity):
    if index-1 < capacity:
        arr[index-1] = element


# Insert an element in open position of the array.
def static_array_open_position(arr, capacity, element):
    for i in range(0, capacity):
        if arr[i] is None:
            arr[i] = element
            break


# Remove an element from array by help of position(1 to n) of element.
def static_array_remove(arr, capacity, index):
    if 0 < index <= capacity:
        arr[index-1] = None


# Insert an element into index after shifting elements to the right.
def static_array_insert_shift(arr, index, capacity, element):
    for w in range(capacity-1, index-1, -1):
        arr[w] =arr[w-1]
    arr[index-1] = element


# Remove value at index before shifting elements to the left.
# No need to 'remove' element, because we already shifted.
def static_array_remove_shift(arr, index, capacity):
    for w in range(index, capacity):
        arr[w-1]= arr[w]
    arr[capacity-1] = None


# Data provide to function call.
box= ["a", "b", "c", "d", "e", "f", "g", "h", None, None]
n = len(box)
i= int(input("which element do you want to print from array: "))
enter = input("Enter the element: ")


# Function call
static_array(box)

static_array_get_element(box, n, i)

static_array_insert(box, i, enter, n)

static_array_remove(box, n, i)

static_array_insert_shift(box, i, n, enter)

static_array_remove_shift(box, i, n)

static_array_open_position(box, n, enter)