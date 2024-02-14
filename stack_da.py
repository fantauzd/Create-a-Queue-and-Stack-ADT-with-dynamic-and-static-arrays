# Name: Dominic Fantauzzo
# OSU Email: fantauzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT Implementation
# Due Date: 2/13/2024
# Description: Implementation of a stack ADT using Dynamic Array.


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack.
        """
        self._da.append(value)

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value. If the stack is
        empty, the method raises a custom “StackException”.
        """
        # Validate that the stack is not empty
        if self._da.length() == 0:
            raise StackException
        # Retrieve the value from the top of the stack
        val = self._da.get_at_index(self._da.length()-1)
        # Remove the value from the top of the stack
        self._da.remove_at_index(self._da.length()-1)
        # Return the value from the top of the stack
        return val

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it. If the
        stack is empty, the method raises a custom “StackException”.
        """
        # Validate that the stack is not empty
        if self._da.length() == 0:
            raise StackException
        # Return the value from the top of the stack without manipulating the stack
        return self._da.get_at_index(self._da.length()-1)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
