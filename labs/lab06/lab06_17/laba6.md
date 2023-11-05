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

<!-- #region -->
<h1> ОТЧЕТ </h1>
<h3> Лабораторная работа №6 <br> <br>
    «Двоичные деревья поиска (Binary Search Tree)» </h3>
<br>
<h4> Цель работы: </h4>
Изучение структуры данных «Двоичное дерево поиска», а также основных операций над ним.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию двоичного дерева поиска в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций над двоичным деревом поиска:
    * формирование бинарного дерева;
    * обход (прямой, симметричный, обратный) бинарного дерева;
    * удаление заданной вершины из бинарного дерева;
    * поиск заданной вершины в бинарном дереве (по значению);
    * печать бинарного дерева на экран;
    * проверка пустоты бинарного дерева;
    * определение высоты бинарного дерева.
3. Реализовать приложение, для работы с бинарным деревом поиска, которое реализует следующий набор действий:
    * инициализация пустого стека;
    * организация диалогового цикла с пользователем;
<br>
<br>
<h4> Code Listing: </h4>

```python
class Node: 
    def __init__(self, data, left = None, right = None)

class BinarySearchTree:
    def __init__(self) #инициализация дерева

    def __str__(self) #вывод дерева

    def push_front(self, data) #добавление элемента в дерево
    
    def pop_front(self) #удаление элемента из дерева

    def clear(self) #очистка дерева
    
    #additions
    def remove(self, length) #удаление нескольких элементов дерева
    
#individuals

    
#Взаимодействие с пользователем
x = input("...")
while (x):
    ///код
    match x:
        case "menu":
            ///код
        
        case "show":
            ///код

        case "add":
            ///код
        
        case "remove":
            ///код

        case "clear":
            ///код
        
        case "stop":
            ///код
    ///код
```
<br>
<h4> Выводы </h4>
В ходе лабораторной работы была изучена структура данных «двоичноe деревo поиска», написана собственнаяя реализация двоичного дерева поиска в виде класса таким образом, что каждая его операция является методом класса. Реализована программа, выполняющая стандартный набор операций с двоичным деревом поиска и приложение, которое осуществляет диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *С чем связана популярность использования деревьев в программировании?* <br>
Деревья являются одной из наиболее эффективных структур данных для хранения и организации информации.
2. *Можно ли список отнести к деревьям?* <br>
Нет, список не является деревом. Список - это упорядоченная коллекция элементов, где каждый элемент имеет свой номер или индекс. В списках элементы могут быть связаны друг с другом только на основе их позиции или индекса. <br>
Дерево же представляет собой иерархическую структуру данных, состоящую из узлов (вершин) и ребер (связей) между ними. Каждый узел в дереве может иметь родителя и ноль или более потомков. Дерево обеспечивает более сложные и гибкие способы организации данных и связей между ними. <br>
Хотя список и дерево могут использоваться для представления и организации данных, они имеют различные свойства и функции, поэтому не могут рассматриваться как одно и то же.
4. *Какие данные содержат адресные поля элемента бинарного дерева?* <br>
Каждый элемент бинарного дерева содержит два адресных поля, которые указывают на его потомков. Эти поля называются "левым потомком" и "правым потомком". <br>
Левый потомок: Это адресное поле, которое указывает на левого потомка элемента. Левый потомок находится "ниже" родительского элемента по отношению к иерархии дерева. <br>
Правый потомок: Это адресное поле, которое указывает на правого потомка элемента. Правый потомок также находится "ниже" родительского элемента в иерархии дерева. <br>
5. *Что такое дерево, двоичное дерево, поддерево?* <br>
Дерево - это иерархическая структура данных, состоящая из вершин (узлов) и ребер (связей) между ними. Каждая вершина может иметь ноль или более потомков, то есть других вершин, которые связаны с ней. Есть одна вершина, из которой начинаются все связи и которая называется корневой вершиной. Каждая вершина может быть связана с одной родительской вершиной, кроме корневой, которая не имеет родителя. <br>
Двоичное дерево - это особый тип дерева, где каждая вершина может иметь не более двух потомков: левый потомок и правый потомок. Левый потомок находится слева от родительской вершины, а правый потомок - справа от нее. <br>
Поддерево - это часть дерева, которая включает вершину и все ее потомки и связи между ними. Вершина, включая всех ее потомков, называется корневой вершиной поддерева. Поддерево может быть любым фрагментом иерархической структуры дерева.
6. *Как рекурсивно определяется дерево?* <br>
Дерево состоит из вершины (корня) и некоторого количества поддеревьев, которые являются деревьями в себе. Поддеревья соединены с корнем вершины. Каждое поддерево определяется таким же рекурсивным правилом.
7. *Какие основные понятия связываются с деревьями?* <br>
    * Корень (Root): Корень дерева - это вершина, которая служит начальной точкой для всего дерева. Она не имеет родителя и является вершиной самого верхнего уровня иерархии.
    * Вершина (Node): Вершина (узел) - это элемент дерева, который содержит некоторую информацию (значение) и связан с другими вершинами (потомками или родителями) через ребра.
    * Ребро (Edge): Ребро - это связь между двумя вершинами в дереве. Ребро может быть направленным или ненаправленным, в зависимости от типа дерева.
    * Потомок (Child): Потомок - это вершина, которая связана с другой вершиной (родителем) напрямую нижнего уровня. Родителю может соответствовать несколько потомков.
    * Родитель (Parent): Родитель - это вершина, от которой исходит ребро, связывающее ее с другой вершиной (потомком). Каждая вершина, за исключением корня, может иметь одного родителя.
    * Потомки (Children): Потомки - это множество вершин, которые связаны с родительской вершиной. У одной вершины может быть любое количество потомков, включая ноль.
    * Путь (Path): Путь представляет собой последовательность ребер, связывающих вершины в дереве. Он определяет путь от одной вершины к другой.
    * Глубина (Depth): Глубина дерева - это количество ребер на пути от корневой вершины до конкретной вершины.
8. *Какие основные операции характерны при использовании деревьев?* <br>
    * Поиск элементов в дереве
    * Добавление элемента в дерево
    * Удаление элемента из дерева
    * Обход дерева.
9. *Как программно реализуется алгоритм операции обхода дерева?* <br>
10. *Как программно реализуется алгоритм операции добавления элемента в дерево?* <br>
11. *Как программно реализуется алгоритм операции удаления элемента из дерева?* <br>
12. *Как программно реализуется  алгоритм операции поиска элемента в дереве?* <br>
<!-- #endregion -->

```python
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    # def print(self, root, level):
    #     if self.is_empty(self.root):
    #         print("binary search tree is empty:", self.root)
    #     else:
    #         if self.is_empty(root):
    #             print("    " * level + "None")
    #         else:
    #             self.print(root.right, level+1)
    #             print("    " * level + str(root.data) + "<")
    #             self.print(root.left, level+1)

    def __str__(self):
        if self.is_empty(self.root):
            return "binary search tree is empty: " + str(self.root)
        else:
            lines, *_ = self.print(self.root)
            for line in lines:
                print(line)
            return ""

    def print(self, root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.is_empty(root.right) and self.is_empty(root.left):
            line = "%s" % root.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.is_empty(root.right):
            lines, n, p, x = self.print(root.left)
            s = "%s" % root.data
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.is_empty(root.left):
            lines, n, p, x = self.print(root.right)
            s = "%s" % root.data
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.print(root.left)
        right, m, q, y = self.print(root.right)
        s = "%s" % root.data
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def is_empty(self, root):
        if root == None:
            return True
        else:
            return False
            
    def add(self, data):
        if self.is_empty(self.root):
            self.root = Node(data)
        else:
            self.add_not_empty(self.root, data)
    
    def add_not_empty(self, root, data):
        if root.data == data:
            raise Exception("Such an element has already been added to the tree")
        # if type(data)!=int:
        #     raise Exception("The tree can't include non-integer elements")
        elif data < root.data:
            if self.is_empty(root.left):
                root.left = Node(data)
            else:
                self.add_not_empty(root.left, data)
        else:
            if self.is_empty(root.right):
                root.right = Node(data)
            else:
                self.add_not_empty(root.right, data)
                
    def pop(self, data):


# try:
#     closing_brackets("({[()]}}")
# except Exception as try_:
#     print(try_)
# finally:
#     code with/without 
   
    def pop_front(self):
        if self.is_empty():
            return "ErRoR"
        else:
            item = self.root
            self.root = item.next
            self.size -= 1
            return item.data

    def direct_traversal(self):
        
    def symmetric_traversal(self):

    def reverse_traversal(self):

    
    def find_item(self, data): #поиск элемента по значению
        temp = self.root
        while (temp != None and temp.data != data):
            temp = temp.next
        if temp == None:
            return False
        else:
            return True

    def depth(self):

    #additions
    def remove(self, length):
        length = int(length)
        if length < 0 or length - 1 > self.size - 1:
            return "ErRoR"
        elif self.is_empty():
            return "empty"
        else:
            for i in range(0, length):
                temp = self.pop_front()

    def clear(self):
        if self.is_empty(self.root):
            return "tree is already empty"
        # temp = self.root
        # while temp != None:
        #     temp.data = None
        #     temp = temp.next
        self.root = None

# #individuals
# case "]":
#     if mytree.get_top() == "[":
#         deleted = mytree.pop_front()
#     else:
#         raise Exception("error")
#         break
# try:
#     closing_brackets("({[()]}}")
# except Exception as try_:
#     print(try_)
# finally:
#     code with/without 



    
# Взаимодействие с пользователем
# x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть стек: введите Show\nЕсли вы хотите проверить пустой ли стек: введите Is Empty\nЕсли вы хотите добавить элементы в стек: введите Add\nЕсли вы хотите удалить элементы из стека: введите Remove\nЕсли вы хотите вывести вершину стека:введите Get Top\nЕсли вы хотите очистить стек: введите Clear\nЕсли вы хотите проверить наличие элемента в стеке: введите Is Item\nЕсли вы хотите развернуть стек: введите Reverse\nЕсли вы хотите закончить: введите Stop\n")
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть дерево: введите Show\nЕсли вы хотите проверить пустое ли дерево: введите Is Empty\nЕсли вы хотите добавить элементы в дерево: введите Add\nЕсли вы хотите удалить элементы из дерева: введите Remove\nЕсли вы хотите очистить дерево: введите Clear\nЕсли вы хотите закончить: введите Stop\n")
mytree = BinarySearchTree()
while True:
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть дерево: введите Show\nЕсли вы хотите проверить пустое ли дерево: введите Is Empty\nЕсли вы хотите добавить элементы в дерево: введите Add\nЕсли вы хотите удалить элементы из дерева: введите Remove\nЕсли вы хотите очистить дерево: введите Clear\nЕсли вы хотите закончить: введите Stop\n")
        case "show":
            print(mytree)
        case "add":
            message = input("Если вы хотите линейно заполнить дерево: введите Fill, если же добавить один элемент: введите Add\n")
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
                        print("Если вдруг вы устанете заполнять дерево и захотите прервать процесс: введите ~I'm LoSeR~")
                        count_elements = 0
                        length = int(length)
                        for i in range(0, length):
                            item = input("Введите элемент: ")
                            if item == "~I'm LoSeR~":
                                print("Элементы успешно добавились, процесс прерван")
                                break
                            else:
                                mytree.add(item)
                                count_elements += 1
                        if count_elements == length:
                            print("Дерево успешно заполнено")
                elif message == "add":
                    item = input("Введите элемент: ")
                    mytree.add(item)
                    print("Вы добавили элемент", item)
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
                    length = input("Введите количество элементов для удаления: ")
       # юююююююю             result = mytree.remove(length)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("В следующий раз стоит вводить корректное количество элементов для удаления :З")
                    elif result == "empty":
                        print("А что вы собрались удалять в пустом дереве (｡· v ·｡)?")
                    else:
                        print("Вы удалили", length, "элементов")
                elif message == "pop":
                    result = mytree.pop_front()
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом дереве (｡· v ·｡)?")
                    else:
                        print("Вы удалили элемент", result)
                else:
                        print("YOU LOSER")
                        print("Вы ввели неправильную команду :З")
        case "clear":
            if mytree.clear() == "tree is already empty":
                print("YOU LOSER")
                print("Не стоит пытаться очистить пустое дерево :З")
            else:
                print("Вы очистили дерево, его элементы больше не доступны :(")
        case "stop":
            break
        case _:
            print("Научись вводить команды правильно :З")
    x = input("Введите еще команду: ")

```

```python
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                for e in range(0,2):
                    f1 = (not(not(y) or ((y and not(z)) and (y or not(e)))) or ((x and w) or (not(w) and x)))
                    f2 = (((not(x) or not(y) or not(z)) and (x or (y and z))) and (not(w) or ((e and w) or (w and not(e)))))
                    if f1 != f2:
                        print(x, y, z, w, e)
```

```python

```
