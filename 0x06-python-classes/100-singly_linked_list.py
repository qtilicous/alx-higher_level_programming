#!/usr/bin/python3
"""
Module of class Singly Linked List.
"""


class Node:
    """
    This class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data in the node.

        Args:
            value (int): The data to store in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the list.

        Returns:
            Node or None: The next node or None if it's the end of the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.

        Args:
            value (Node or None):
            The next node or None if it's the end of the list.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new singly linked list with an empty head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Provides a string representation of the singly linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
