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
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
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
        if not data.isdigit():
            raise TypeError("Only numbers can be added to the tree")
        data = int(data)
        if self.is_empty(self.root):
            self.root = Node(data)
        else:
            self.add_not_empty(self.root, data)

    def add_not_empty(self, root, data):
        if root.data == data:
            raise ValueError("Such an element has already been added to the tree")
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

    #individuals
    def product_of_elements_even_levels(self):
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        result = 1
        result *= self.product_of_elements_even_levels_root(self.root, result, True)
        return result

    def product_of_elements_even_levels_root(self, root, result, flag):
        if not self.is_empty(root):
            if flag:
                result *= root.data
                result *= self.product_of_elements_even_levels_root(root.right, 1, not flag)
                result *= self.product_of_elements_even_levels_root(root.left, 1, not flag)
            else:
                result *= self.product_of_elements_even_levels_root(root.right, 1, not flag)
                result *= self.product_of_elements_even_levels_root(root.left, 1, not flag)
        return result
        
a = BinarySearchTree()
a.add("9")
a.add("5")
a.add("2")
a.add("1")
a.add("4")
a.add("8")
a.add("7")
a.add("12")
a.add("10")
a.add("11")
a.add("14")
a.add("13")
print(a)
print(a.product_of_elements_even_levels())
```

```python

```
