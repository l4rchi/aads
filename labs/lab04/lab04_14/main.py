class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("Список пуст.")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.head = new_node

    def pop_front(self):
        if self.is_empty():
            print("Список пуст. Невозможно удалить элемент из начала.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def pop_back(self):
        if self.is_empty():
            print("Список пуст. Невозможно удалить элемент из конца.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    def at(self, index):
        if self.is_empty():
            print("Список пуст. Невозможно получить элемент по индексу.")
            return None

        current = self.head
        for _ in range(index):
            current = current.next
            if current == self.head:
                print(f"Индекс {index} выходит за пределы списка.")
                return None

        return current.data

    def push(self, data, index):
        if index == 0:
            self.push_front(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
                if current == self.head:
                    print(f"Индекс {index} выходит за пределы списка.")
                    return

            new_node.next = current.next
            current.next = new_node

    def pop(self, index):
        if self.is_empty():
            print("Список пуст. Невозможно удалить элемент по индексу.")
            return

        if index == 0:
            self.pop_front()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
                if current == self.head:
                    print(f"Индекс {index} выходит за пределы списка.")
                    return

            if current.next == self.head:
                print(f"Индекс {index} выходит за пределы списка.")
                return

            current.next = current.next.next

    def clear(self):
        self.head = None


def main():
    cll = CircularLinkedList()

    while True:
        print("\nМеню:")
        print("1. Вставка элемента в начало списка")
        print("2. Вставка элемента в конец списка")
        print("3. Удаление элемента из начала списка")
        print("4. Удаление элемента из конца списка")
        print("5. Вывод элемента по индексу")
        print("6. Вставка элемента по индексу")
        print("7. Удаление элемента по индексу")
        print("8. Очистка списка")
        print("9. Отобразить список")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            data = input("Введите значение элемента: ")
            cll.push_front(data)
        elif choice == '2':
            data = input("Введите значение элемента: ")
            cll.push_back(data)
        elif choice == '3':
            cll.pop_front()
        elif choice == '4':
            cll.pop_back()
        elif choice == '5':
            index = int(input("Введите индекс элемента: "))
            value = cll.at(index)
            if value is not None:
                print(f"Элемент по индексу {index}: {value}")
        elif choice == '6':
            index = int(input("Введите индекс элемента: "))
            data = input("Введите значение элемента: ")
            cll.push(data, index)
        elif choice == '7':
            index = int(input("Введите индекс элемента для удаления: "))
            cll.pop(index)
        elif choice == '8':
            cll.clear()
        elif choice == '9':
            cll.display()
        elif choice == '0':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")


if __name__ == "__main__":
    main()
