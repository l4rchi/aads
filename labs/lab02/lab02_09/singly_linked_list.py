class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_front(self):
        if self.head is None:
            return None
        old_head = self.head
        data = old_head.data
        if self.length == 1:
            self.head = None
        else:
            self.head = old_head.next
        self.length -= 1
        return data

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def pop_back(self):
        if self.head is None:
            return None

        if self.length == 1:
            data = self.head.data
            self.head = None
            self.length -= 1
            return data

        current = self.head
        while current.next.next:
            current = current.next

        data = current.next.data
        current.next = None
        self.length -= 1
        return data

    def at(self, index):
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def push(self, data, index):
        if index == 0:
            self.push_front(data)
        elif index == self.length:
            self.push_back(data)
        elif index > 0 and index < self.length:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
        else:
            raise IndexError("Index out of range")

    def pop(self, index):
        if index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()
        elif index > 0 and index < self.length - 1:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node_to_remove = current.next
            current.next = node_to_remove.next
            data = node_to_remove.data
            del node_to_remove
            self.length -= 1
            return data
        else:
            raise IndexError("Index out of range")

    def clear(self):
        while self.head:
            node_to_remove = self.head
            self.head = self.head.next
            del node_to_remove
        self.length = 0

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


def intersect_lists(list1, list2):
    intersection = List()

    current1 = list1.head
    while current1:
        current2 = list2.head
        while current2:
            if current1.data == current2.data:
                intersection.push_back(current1.data)
            current2 = current2.next
        current1 = current1.next

    return intersection


def multiply_lists(list1, list2):
    result = List()

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        result.push_back(current1.data * current2.data)
        current1 = current1.next
        current2 = current2.next

    return result


my_list = List()
my_list.push_back(1)
my_list.push_back(2)
my_list.push_back(3)

for item in my_list:
    print(item, end=' -> ')
print("None")

print("Element at index 1:", my_list.at(1))
my_list.push(4, 2)
my_list.display()  # 1 -> 2 -> 4 -> 3 -> None
removed_data = my_list.pop(2)
print("Removed data:", removed_data)
my_list.display()  # 1 -> 2 -> 3 -> None
my_list.clear()
my_list.display()  # None
