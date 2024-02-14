# Name: Dominic Fantauzzo
# OSU Email: fantauzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2 - Dynamic Array Implementation
# Due Date: 2/6/2024
# Description: Implementation of a dynamic array, using a static array module.
#              The dynamic array behaves similarly to a python list, with limited functionality.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        If the new capacity is a positive integer that is less than the size of the dynamic array
        then the function creates a new larger static array with the desired capacity and copies any
        elements, in order, from the older static array. Finally, the function assigns the dynamic array to
        the new, resized, static array.

        :param new_capacity: an integer

        :return: None
        """
        # ensure array can be resized to new capacity
        if new_capacity <= 0 or new_capacity < self._size:
            return
        else:
            # Create a new static array.
            new_array = StaticArray(new_capacity)
            # Copy over any elements of previous array
            for i in range(self._size):
                new_array[i] = self._data[i]
            # update the dynamic array to the new static array, freeing unused memory
            self._data = new_array
            self._capacity = new_array.length()

    def append(self, value: object) -> None:
        """
        Appends the value argument to the end of the dynamic array.
        Doubles the size of the array before appending, if space is needed.

        :param value: an object to append

        :return: None
        """
        # If there is extra space, add the element
        if self._size < self._capacity:
            self._data[self._size] = value
            self._size = self._size + 1
        # If full, resize then add the element
        else:
            self.resize(self._capacity * 2)
            self._data[self._size] = value
            self._size = self._size + 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a value at a desired index in the array by shifting the value at the desired index,
        and any subsequent values, to the right.

        :param index: an integer representing an index

        :param value: object

        :return: None
        """
        # Ensure index is viable
        if index < 0 or index > self._size:
            raise DynamicArrayException
        # Ensure there is room to add value, double size if full
        if self._size >= self._capacity:
            self.resize(self._capacity*2)
        # Create a temporary static array to store values that will be moved
        if self._size - index < 1:
            self.append(value)
            return
        else:
            temp_array = StaticArray(self._size - index)
            pos = index
            for val in range(temp_array.length()):
                temp_array[val] = self._data[pos]
                pos += 1
        # insert the value at the desired index, record size increase
            self._data[index] = value
            self._size += 1
        # append the stored values in order following the inserted value, stop once a None value is encountered
            index += 1
            for val in range(temp_array.length()):
                    self._data[index + val] = temp_array[val]


    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at the specified index in the dynamic array and updates
        the size attribute accordingly. Slides any subsequent values leftward to fill hole.

        :param index: an integer representing an index

        :return: None
        """
        # Ensure index is viable
        if index < 0 or index > (self._size-1):
            raise DynamicArrayException
        # If the array is oversized, adjust the capacity. Never reduce capacity below 10.
        if self._size < (self._capacity/4):
            if self._capacity > 10 and self._size >= 5:
                self.resize(self._size*2)
            elif self._capacity > 10:
                self.resize(10)
        # if removing the last value in the array, simply set it to None
        # Ensures best case is in O(1)
        if index == self._size - 1:
            self._data[index] = None
            self._size -= 1
        # Create a temporary static array to store values that will be moved
        else:
            temp_array = StaticArray(self._size - (index+1))
            pos = index + 1
            for val in range(temp_array.length()):
                temp_array[val] = self._data[pos]
                pos += 1
            # overwrite the removed value by shifting all rightward values to the left
            for val in range(temp_array.length()):
                self._data[index + val] = temp_array[val]
            self._size -= 1


    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new DynamicArray object that contains the requested number of elements
        from the original array, starting with the element located at the requested start index.

        :param start_index: integer representing the index with the first element we want returned

        :param size: integer representing the number of values in the new array

        :return: a new dynamic array
        """
        if size < 0 or start_index < 0 or start_index >= self._size or start_index+size > self._size:
            raise DynamicArrayException
        else:
            new_array = DynamicArray()
            for val in range(size):
                new_array.append(self._data[start_index+val])
            return new_array

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Takes another DynamicArray object as a parameter, and appends all elements
        from this array onto the current one, in the same order in which they are stored in the input array.

        :param second_da: a dynamic array

        :return: None
        """
        # merge two lists, stable
        for val in range(second_da._size):
            self.append(second_da._data[val])

    def map(self, map_func) -> "DynamicArray":
        """
        Creates a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.

        :param map_func: a function

        :return: a new dynamic array
        """
        # Create new dynamic array
        new_array = DynamicArray()
        # for each value, apply the function parameter then append to the new array
        for val in range(self._size):
            new_array.append(map_func(self._data[val]))
        return new_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True

        :param filter_func: a filter function

        :return: a new dynamic array
        """
        # Create new dynamic array
        new_array = DynamicArray()
        # for each value, if the filter function returns true, append to the new array
        for val in range(self._size):
            if filter_func(self._data[val]):
                new_array.append(self._data[val])
        return new_array


    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Applies the reduce_func to all elements of the dynamic array and returns the resulting value.

        :param reduce_func: the reduce function
        :param initializer: the initial value (optional)

        :return: the resultant object
        """
        # use a variable to track if the first value in the list will be the initializer
        pos = 0
        # If the array is empty, return the initializer
        if self._size == 0:
            return initializer
        # If the initializer parameter is passed, save it later
        if initializer != None:
            result = initializer
        # If no initializer is passed and array is not empty, use the first element
        if initializer == None:
            result = self._data[0]
            # If the first element is the initializer, we don't use it in the reduce function
            pos += 1
        # Iterate through the array and perform the reduce function on each result
        for val in range(pos, self._size):
            result = reduce_func(result, self._data[val])
        return result


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Receives a dynamic array already in sorted order, either non-descending or non-ascending.
    The function will return a tuple containing (in this order) a dynamic array comprising
    the mode (most-occurring) value/s of the array, and an integer that represents the highest
    frequency (how many times they appear).

    :param arr: a sorted dynamic array

    :return: a tuple with the array of modes and their frequency
    """
    # Create variables to store the initial mode, mode frequency, and the current element and its frequency
    mode = arr._data[0]
    modeFreq = 0
    el = None
    elFreq = 0
    # Create a dynamic array to store mode(s)
    new_arr = DynamicArray()
    new_arr.append(mode)
    # Increment mode frequency or element frequency when we iterate over like elements.
    # When iterating over new elements, compare the frequency of the last element with mode
    # and update the dynamic array of modes if appropriate.
    for num in range(arr._size):
        if arr._data[num] == mode:
            modeFreq += 1
        elif arr._data[num] == el:
            elFreq += 1
        else:
            # Elements of the same frequency as the current mode are appended
            if elFreq == modeFreq:
                new_arr.append(el)
            # Elements with a higher frequency mean that all previous modes are forgotten
            # and a new dynamic array of modes is created
            elif elFreq > modeFreq:
                new_arr = DynamicArray()
                new_arr.append(el)
                modeFreq = elFreq

            el = arr._data[num]
            elFreq = 1
    # perform final check to see if last element was mode
    if elFreq == modeFreq:
        new_arr.append(el)
    elif elFreq > modeFreq:
        new_arr = DynamicArray()
        new_arr.append(el)
        modeFreq = elFreq

    return (new_arr, modeFreq)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
