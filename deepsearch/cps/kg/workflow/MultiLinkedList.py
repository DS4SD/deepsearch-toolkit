from collections import OrderedDict
from uuid import uuid4


class Node:
    def __init__(self, data, id=None):
        self.id = id or str(uuid4())
        self.data = data
        self.next = None
        self.prev = None
        self.child = None


class MultiLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def __eq__(self, other):
        return self.head == other

    def __ne__(self, other):
        return self.head != other

    def append(self, value):
        if isinstance(value, Node):
            new_node = value
        else:
            new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            last = self.tail
            last.next = new_node
            new_node.prev = last
            self.tail = new_node

    def append_child(self, child=None):
        if not self.tail.child:
            self.tail.child = []
        if not isinstance(child, Node):
            child = Node(child)

        self.tail.child.append(child)

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data, tmp.child, "\n")
            tmp = tmp.next

    def flatten_list(self):
        if not self.head:
            return

        current_node = self.head
        result = {}

        # One by one traverse through all nodes
        # of first level linked list
        # till we reach the tail node
        while current_node is not None:
            # If current node has a child
            if current_node.child:
                # append the child list
                for child in current_node.child:
                    # skip child with no data, used to mark the parent node
                    if not child.data and child.next:
                        child = child.next
                    # if node already visited, dont proccess them again
                    if child.id in result:
                        continue

                    # append the child
                    temp = current_node.next
                    current_node.next = child
                    found_tail = child
                    # find tail
                    while found_tail.next:
                        found_tail = found_tail.next
                    # connect the tail of child to next
                    found_tail.next = temp
                    if temp:
                        temp.prev = found_tail

                current_node.child = None  # remove childs

            result.update({current_node.id: current_node.data})
            # Change current node
            current_node = current_node.next

        return result
