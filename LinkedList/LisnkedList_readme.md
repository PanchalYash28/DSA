# Java LinkedList Implementation

This project provides a simple implementation of a singly linked list in Java. It demonstrates the basic operations typically supported by a linked list data structure.

## Features

- Add elements to the list
- Remove the first element
- Remove the last element
- Remove an element at a specific index
- Find the length of the list
- Reverse the list
- Print all elements in the list

## Structure

The project consists of the following classes:

### 1. `Node`

Represents a single element in the linked list with:
- `data`: integer value of the node
- `next`: reference to the next node

### 2. `MyLinkedList`

Handles core linked list operations:
- `add(int data)`: Adds a new node at the end
- `print()`: Displays all node values
- `RemoveFirstElement()`: Deletes the first node
- `RemoveElementFromLast()`: Deletes the last node
- `RemoveIndexedElement(int index)`: Deletes the node at a specified index
- `FindLength()`: Returns the count of nodes in the list
- `ReverseOfLinkedList()`: Reverses the list in-place

### 3. `LinkedList`

Contains the `main` method to test all functionalities.


## How to Run

1. Clone the repository.
2. Compile the Java file:
   ```bash
   javac LinkedList.java

java LinkedList

output :-

![image](https://github.com/user-attachments/assets/6902574c-e3a2-41e7-95c7-d0920167ffae)

