class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop_front(self):
        if not self.head:
            print("List is empty, cannot pop from front.")
            return
        self.head = self.head.next

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop_back(self):
        if not self.head:
            print("List is empty, cannot pop from back.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def at(self, index):
        if index < 0:
            print("Invalid index")
            return None
        current = self.head
        for _ in range(index):
            if current is None:
                print("Invalid index")
                return None
            current = current.next
        return current.data

    def push(self, data, index):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.push_front(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Invalid index")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def pop(self, index):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.pop_front()
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                print("Invalid index")
                return
            current = current.next
        current.next = current.next.next

    def clear(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def print_menu():
    print("1. Инициализация пустого списка")
    print("2. Добавить элемент в начало списка")
    print("3. Удалить элемент из начала списка")
    print("4. Добавить элемент в конец списка")
    print("5. Удалить элемент с конца списка")
    print("6. Получить элемент по индексу")
    print("7. Добавить элемент по индексу")
    print("8. Удалить элемент по индексу")
    print("9. Очистить список")
    print("10. Вывести список")
    print("0. Выход")


def main():
    linked_list = LinkedList()

    while True:
        print_menu()
        choice = input("Выберите действие (введите число): ")

        if choice == "1":
            linked_list = LinkedList()
            print("Список инициализирован.")
        elif choice == "2":
            data = input("Введите элемент для добавления в начало списка: ")
            linked_list.push_front(data)
            print("Элемент добавлен.")
        elif choice == "3":
            linked_list.pop_front()
            print("Элемент удален из начала списка.")
        elif choice == "4":
            data = input("Введите элемент для добавления в конец списка: ")
            linked_list.push_back(data)
            print("Элемент добавлен в конец списка.")
        elif choice == "5":
            linked_list.pop_back()
            print("Элемент удален с конца списка.")
        elif choice == "6":
            index = int(input("Введите индекс элемента: "))
            element = linked_list.at(index)
            if element is not None:
                print(f"Элемент по индексу {index}: {element}")
        elif choice == "7":
            data = input("Введите элемент для добавления: ")
            index = int(input("Введите индекс, куда добавить элемент: "))
            linked_list.push(data, index)
            print("Элемент добавлен по индексу.")
        elif choice == "8":
            index = int(input("Введите индекс элемента для удаления: "))
            linked_list.pop(index)
            print("Элемент удален по индексу.")
        elif choice == "9":
            linked_list.clear()
            print("Список очищен.")
        elif choice == "10":
            print("Текущий список:")
            linked_list.display()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    main()
