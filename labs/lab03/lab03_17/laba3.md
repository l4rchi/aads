---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # def print(self):
    #     if self.head == None:
    #         print("list is empty:", self.size, self.head)
    #     else:
    #         temp = self.head
    #         print("list size =", self.size)
    #         print("head is =", self.head.data)
    #         print ("list:", end = " ")
    #         while temp:
    #             print(temp.data, end = " ")
    #             temp = temp.next
    #         print()

    def __str__(self):
        if self.head == None:
            text = "list is empty: " + str(self.size) + " " + str(self.head)
        else:
            text = "list size = " + str(self.size) + "\nhead is = " + str(self.head.data) + "\nlist: "
            temp = self.head
            while temp:
                text += str(temp.data) + " "
                temp = temp.next
        return text

    def push_back(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else:
            temp = self.tail
            temp.next = item
            item.next = None
            item.prev = temp
            self.tail = item
        self.size += 1
    
    def push_front(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else:
            temp = self.head
            temp.prev = item
            item.prev = None
            item.next = temp
            self.head = item
        self.size += 1

    def insert(self, index, data):
        if not(index.isdigit()):
            return "ErRoR"
        index = int(index)
        if index < 0:
            index += self.size
        if index < 0 or index > self.size:
            return "ErRoR"
        elif self.head == None or index == self.size:
            self.push_back(data)
        elif index == 0:
            self.push_front(data)
        else:
            item = Node(data)
            temp = self.head
            count = 0
            while (count < index - 1):
                temp = temp.next
                count += 1
            curr = temp.next
            temp.next = item
            item.prev = temp
            item.next = curr
            curr.prev = item
            self.size += 1

    def find_item(self, data): #поиск элемента по значению
        temp = self.head
        index = 0
        while (temp != None and temp.data != data):
            index += 1
            temp = temp.next
        if temp == None:
            return "ErRoR"
        else:
            return index

    def find_index(self, index): #поиск элемента по индексу
        if not(index.isdigit()):
            return "ErRoR"
        index = int(index)
        if index < 0:
            index += self.size
        if index > self.size - 1 or index < 0:
            return "ErRoR"
        temp = self.head
        count = 0
        while (count < index):
            temp = temp.next
            count += 1
        return temp.data

    def pop_front(self):
        if self.head == None:
            return "ErRoR"
        else:
            item = self.head
            self.head = item.next
            self.head.prev = None
            self.size -= 1
            return item.data

    def pop_back(self):
        if self.head == None:
            return "ErRoR"
        else:
            item = self.tail
            self.tail = item.prev
            self.tail.next = None
            self.size -= 1
            return item.data

    def pop(self, index):
        if not(index.isdigit()):
            return "ErRoR"
        index = int(index)
        if index < 0:
            index += self.size
        if index < 0 or index > self.size - 1:
            return "ErRoR"
        elif self.head == None or index == self.size - 1:
            return self.pop_back()
        elif index == 0:
            return self.pop_front()
        else:
            temp = self.head
            count = 0
            while (count < index - 1):
                temp = temp.next
                count += 1
            item = temp.next
            temp.next = item.next
            item.next.prev = temp
            self.size -= 1
            return item.data

    def remove(self, index, length):
        if (not index.isdigit()) or (not length.isdigit()):
            return "ErRoR"
        index = int(index)
        length = int(length)
        if index + length < 0 or index + length - 1 > self.size - 1:
            return "ErRoR"
        elif self.head == None:
            return "empty"
        else:
            for i in range(0, length):
                index = str(index)
                temp = self.pop(index)

    def reverse(self):
        if self.head == None:
            return "ErRoR"
        previous = self.head
        current = previous.next
        head = self.head
        tail = self.tail
        while (current != None):
            next = current.next
            current.next = previous
            previous.prev = current
            previous = current
            current = next
        self.head = tail
        self.head.prev = None
        self.tail = head
        self.tail.next = None

    def clear(self):
        if self.head == None:
            return "list is already empty"
        temp = self.head
        while temp != None:
            temp.data = None
            temp = temp.next
        self.size = 0
        self.head = None

    # Мне было скучно
    def count(self, item): #Подсчет количества элементов с заданным значением
        if self.head == None:
            return "ErRoR"
        else:
            count = 0
            temp = self.head
            while temp != None:
                if temp.data == item:
                    count += 1
                temp = temp.next
            if count == 0:
                return "ErRoR 404"
            else:
                return count

    def sort(self): #Сортировка списка
        if self.head == None:
            return "NoNo"
        else:
            sorted = []
            temp = self.head
            while temp != None:
                sorted += [temp.data]
                temp = temp.next
            sorted.sort()
            self.clear()
            for i in sorted:
                self.push_back(i)
        return self

#Индивидуальное задание 1-17
# def 

#Индивидуальное задание 2-17
# def no_triple_numbers(mylist):
    

# Взаимодействие с пользователем
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть список: введите Show\nЕсли вы хотите добавить элементы в список: введите Add\nЕсли вы хотите удалить элементы из списка: введите Remove\nЕсли вы хотите найти элемент в списке: введите Find Value\nЕсли вы хотите вывести определенный элемент из списка: введите Find Index\nЕсли вы хотите развернуть список: введите Reverse\nЕсли вы хотите очистить список: введите Clear\nЕсли вы хотите сложить два списка: введите Concatenation\nЕсли вы хотите удалить из списка все элементы, которых больше двух: введите No Triple Elements\nЕсли вы хотите узнать количество вхождений некоторого элемента: введите Count\nЕсли вы хотите отсортировать список: введите Sort\nЕсли вы хотите закончить: введите Stop\n")
mylist = Doubly_Linked_List()
while (x):
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть список: введите Show\nЕсли вы хотите добавить элементы в список: введите Add\nЕсли вы хотите удалить элементы из списка: введите Remove\nЕсли вы хотите найти элемент в списке: введите Find Value\nЕсли вы хотите вывести определенный элемент из списка: введите Find Index\nЕсли вы хотите развернуть список: введите Reverse\nЕсли вы хотите очистить список: введите Clear\nЕсли вы хотите сложить два списка: введите Concatenation\nЕсли вы хотите удалить из списка все элементы, которых больше двух: введите No Triple Elements\nЕсли вы хотите узнать количество вхождений некоторого элемента: введите Count\nЕсли вы хотите отсортировать список: введите Sort\nЕсли вы хотите закончить: введите Stop")
        case "show":
            # mylist.print()
            print(mylist)
        case "add":
            message = input("Если вы хотите линейно заполнить список: введите Fill, если же добавить один элемент по индексу: введите Add\n")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                if message == "fill":
                    length = input("Введите количество элементов которое хотите добавить: ")
                    if not length.isdigit():
                        print("YOU LOSER")
                        print("Надо было ввести число :З")
                    else:
                        print("Если вдруг вы устанете заполнять список и захотите прервать процесс: введите ~I'm LoSeR~")
                        count_elements = 0
                        length = int(length)
                        flag = True
                        for i in range(0, length):
                            if not flag:
                                break
                            item = input("Введите элемент: ")
                            if item == "~I'm LoSeR~":
                                while True:
                                    exit = input("Если вы хотите закончить заполнение списка: введите Break, если добавить элемент ~I'm LoSeR~: введите Add\n")
                                    if not exit.isalpha():
                                        print("YOU LOSER")
                                        print("Надо было ввести команду :З")
                                        print("Попробуйте еще раз")
                                    else:
                                        exit = exit.lower() 
                                        if exit == "break":
                                            print("Элементы успешно добавились, процесс прерван")
                                            flag = False
                                            break
                                        elif exit == "add":
                                            result = mylist.push_back(item)
                                            count_elements += 1
                                            break
                                        else:
                                            print("YOU LOSER")
                                            print("Надо было ввести команду :З")
                                            print("Попробуйте еще раз")
                            else:
                                mylist.push_back(item)
                                count_elements += 1
                        if count_elements == length:
                            print("Список успешно заполнен")
                elif message == "add":
                    index = input("Введите индекс: ")
                    item = input("Введите элемент: ")
                    if mylist.insert(index, item) == "ErRoR":
                        print("YOU LOSER")
                        print("Не вводите некорректный индекс :З")
                    else:
                        print("Вы добавили элемент", item, "по индексу", index)
                else:
                    print("YOU LOSER")
                    print("Вы ввели неправильную команду :З")
        case "remove":
            message = input("Если вы хотите удалить несколько элементов: введите Remove, если один: введите Pop")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                message = message.lower()
                if message == "remove":
                    index = input("Введите индекс, с которого начинать удаление элементов: ")
                    length = input("Введите количество элементов для удаления: ")
                    result = mylist.remove(index, length)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("В следующий раз стоит вводить корректный индекс и длину :З")
                    elif result == "empty":
                        print("А что вы собрались удалять в пустом списке (｡· v ·｡)?")
                    else:
                        print("Вы удалили", length, "элементов, начиная с индекса", index)
                elif message == "pop":
                    index = input("Введите индекс: ")
                    result = mylist.pop(index)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("Не вводите некорректный индекс :З")
                    else:
                        print("Вы удалили элемент", result)
                else:
                        print("YOU LOSER")
                        print("Вы ввели неправильную команду :З")
        case "find value":
            value = input("Введите элемент: ")
            result = mylist.find_item(value)
            if result == "ErRoR":
                print("YOU LOSER")
                print("Не ищите элемент, которого нет в списке :З")
            else:
                print("Элемент", value, "находится в списке под индексом", result)
        case "find index":
            index = input("Введите индекс: ")
            result = mylist.find_index(index)
            if result == "ErRoR":
                print("YOU LOSER")
                print("Не вводите некорректный индекс :З")
            else:
                print("Под индексом", index, "в списке находится элемент", result)
        case "reverse":
            if mylist.reverse() == "ErRoR":
                print("YOU LOSER")
                print("Не пытайтесь развернуть пустой список :З")
            else:
                print("Вы развернули список")
        case "clear":
            if mylist.clear() == "list is already empty":
                print("YOU LOSER")
                print("Не стоит пытаться очистить пустой список :З")
            else:
                print("Вы очистили список, его элементы больше не доступны :(")
        case "concatenation":
            print("Создайте список, который хотите присоединить:")
            length = input("Введите длину списка: ")
            mylist2 = Doubly_Linked_List()
            if not length.isdigit():
                print("YOU LOSER")
                print("Надо было ввести число :З")
            elif int(length) == 0:
                print("Результат сложения списков:")
                # list_concatenation(mylist, mylist2).print()
                print(list_concatenation(mylist, mylist2))
            else:
                print("Если вдруг вы устанете заполнять список и захотите прервать процесс: введите ~I'm LoSeR~")
                count_elements = 0
                length = int(length)
                flag = True
                for i in range(0, length):
                    if not flag:
                        break
                    item = input("Введите элемент: ")
                    if item == "~I'm LoSeR~":
                        while flag:
                            exit = input("Если вы хотите закончить заполнение списка: введите Break, если добавить элемент ~I'm LoSeR~: введите Add\n")
                            if not exit.isalpha():
                                print("YOU LOSER")
                                print("Надо было ввести команду :З")
                                exit = input("Попробуйте еще раз: ")
                            else:
                                exit = exit.lower() 
                                if exit == "break":
                                    mylist2.clear()
                                    print("Список для присоединения теперь снова пустой, для сложения списков пропишите команду еще раз")
                                    flag = False
                                    break
                                elif exit == "add":
                                    result = mylist2.push_back(item)
                                    count_elements += 1
                                    break
                                else:
                                    print("YOU LOSER")
                                    print("Надо было ввести команду :З")
                                    print("Попробуйте еще раз")
                    else:
                        result = mylist2.push_back(item)
                        count_elements += 1
                if count_elements == length:
                    print("Поздравляем, второй список успешно создан")
                    print("Результат сложения списков:")
                    # list_concatenation(mylist, mylist2).print()
                    print(list_concatenation(mylist, mylist2))
        case "no triple elements":
            result = no_triple_numbers(mylist)
            if result == "ErRoR":
                print("YOU LOSER")
                print("Не пытайтесь почистить пустой список :З")
            else:
                print("Список успешно почищен")
                # result.print()
                print(result)
        case "count":
            item = input("Введите элемент, количество вхождений которого хотите узнать: ")
            result = mylist.count(item)
            if result == "ErRoR":
                print("Что вы собрались искать в пустом списке (｡· v ·｡)?")
            elif result == "ErRoR 404":
                print("ErRoR 404")
            else:
                print("Элемент", item, "встретился в списке", result, "раз")
        case "sort":
            result = mylist.sort()
            if result == "NoNo":
                print("YOU LOSER")
                print("Не надо пытаться отсортировать пустой список :З")
            else:
                # result.print()
                print(result)
        case "stop":
            break
    x = input("Введите еще команду: ")

# # tests
# list1 = Doubly_Linked_List()
# list1.print()
# print("###test_push_front###")
# list1.push_front(333)
# list1.push_front(22)
# list1.push_front(1)
# list1.print()
# print("###test_push_back###")
# list1.push_back(4)
# list1.push_back(55)
# list1.push_back(666)
# list1.print()
# print("###test_insert###")
# list1.insert(7, "fail")
# list1.insert(6, "last")
# list1.insert(0 , "first")
# list1.insert(3, "insert")
# list1.print()
# print("###test_find_item###")
# print(list1.find_item("gg"))
# print(list1.find_item(11))
# print(list1.find_item("insert"))
# print(list1.find_item(22))
# list1.print()
# print("###test_find_index###")
# print(list1.find_index(-2))
# print(list1.find_index(4))
# print(list1.find_index(10))
# print(list1.find_index(-10))
# list1.print()
# print("###test_pop_front###")
# print(list1.pop_front())
# print(list1.pop_front())
# list2 = Doubly_Linked_List()
# print(list2.pop_front())
# list1.print()
# list2.print()
# print("###test_pop_back###")
# print(list1.pop_back())
# print(list1.pop_back())
# list2 = Doubly_Linked_List()
# print(list2.pop_back())
# list1.print()
# list2.print()
# print("###test_pop###")
# print(list1.pop(-4))
# print(list1.pop(-5))
# print(list1.pop(5))
# list2 = Doubly_Linked_List()
# print(list2.pop(0))
# print(list1.pop(4))
# print(list1.pop(0))
# list1.print()
# list2.print()
# print("###test_reverse###")
# list1.print()
# list1.reverse()
# list1.print()
# list2 = Doubly_Linked_List()
# list2.reverse()
# list2.print()
# print("###test_clear###")
# list1.print()
# list1.clear()
# list1.print()
# list2 = Doubly_Linked_List()
# list2.clear()
# list2.print()
# print("###test_list_concatenation###")
# list1 = Doubly_Linked_List()
# list2 = Doubly_Linked_List()
# list1.push_front(333)
# list1.push_front(22)
# list1.push_front(1)
# list2.push_back(4)
# list2.push_back(55)
# list2.push_back(666)
# list_concatenation(list1, list2).print()
# list3 = Doubly_Linked_List()
# list4 = Doubly_Linked_List()
# list_concatenation(list3, list4).print()
# list_concatenation(list1, list4).print()
# list_concatenation(list3, list2).print()
# print("###test_no_triple_numbers###")
# list1 = Doubly_Linked_List()
# list2 = Doubly_Linked_List()
# list1.push_front(333)
# list1.push_front(22)
# list1.push_front(333)
# list1.push_front(22)
# list1.push_front(1)
# list1.push_front(22)
# list1.push_front(0)
# list1.print()
# no_triple_numbers(list1)
# list1.print()
```

```python

```
