# Name: Dominic Fantauzzo
# OSU Email: fantauzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT Implementation
# Due Date: 2/13/2024
# Description: Implementation of  a Singly Linked List data structure with the
# following methods: insert_front(), insert_back(), insert_at_index(), remove_at_index(), remove(),
# count(), find(), slice()


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel) in O(1) time.
        """
        new_node = SLNode(value)
        # attach node to front of list (or None) before adjusting sentinel
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list in O(N) time.
        """
        # Start at sentinel and find last node (where next is None)
        node = self._head
        while node.next:
            node = node.next
        # Create new node and attach at end
        node.next = SLNode(value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts a new value at the specified index position in the linked list in O(N) time.
        """
        # Validate index
        if index < 0 or index > self.length():
            raise SLLException
        # Traverse the linked list so the node at pos is before the index
        pos = self._head
        for i in range(index):
            pos = pos.next
        # Insert a new node at the index
        new_node = SLNode(value)
        new_node.next = pos.next
        pos.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list.
        """
        # Validate index
        if index < 0 or index > self.length()-1:
            raise SLLException
        # Traverse the linked list so the node at pos is before the index
        pos = self._head
        for i in range(index):
            pos = pos.next
        # Alter the link to skip the node at index, removing it
        pos.next = pos.next.next

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end, and removes the first node
        that matches the provided value. The method returns True if a node was removed from the
        list. Otherwise, it returns False.
        """
        # use variables to hold value of 2 nodes
        node_a = self._head
        node_b = node_a.next
        # Iterate until the left variable is on the last node
        while node_b is not None:
            # Use the right node to search for the target value so even the last node is searched
            if node_b.value == value:
                node_a.next = node_b.next
                return True
            # Shift the pair of nodes rightward
            node_a = node_a.next
            node_b = node_b.next
        # If no node was found, return False
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided value.
        The method then returns this number
        """
        node = self._head.next
        count = 0
        # Iterate over each node in the linked list
        while node is not None:
            # increment count when a match is found
            if node.value == value:
                count += 1
            node = node.next
        return count

    def find(self, value: object) -> bool:
        """
        This method returns a Boolean value based on whether the provided value exists in the list.
        """
        node = self._head.next
        # Iterate over each node in the linked list
        while node is not None:
            # Return True if we found a match
            if node.value == value:
                return True
            node = node.next
        # Return False when there is nothing left to check
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList that contains the requested number of nodes from the
        original list, starting with the node located at the requested start index
        """
        # validate index and size parameters
        if start_index < 0 or start_index > self.length()-1 or start_index+size > self.length() or size < 0:
            raise SLLException
        # Traverse the linked list so pos holds the node at index
        pos = self._head.next
        for i in range(start_index):
            pos = pos.next
        # Initialize a new linked list
        new_list = LinkedList()
        # Continue adding values to tha back of the linked list based on the size parameter
        for i in range(size):
            new_list.insert_back(pos.value)
            pos = pos.next
        return new_list


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
