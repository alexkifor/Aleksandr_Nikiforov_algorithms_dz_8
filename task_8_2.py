class BinaryError(Exception):
    def __init__(self, root, new_val, left=True or False, right=True or False):
        self.root = root
        self.new_val = new_val
        self.left = left
        self.right = right

    def __str__(self):
        if self.left == True:
            return f"недопустимое значение для бинарного дерева: {self.new_val}," \
                    f"введите значение меньше чем {self.root}"
        elif self.right == True:
            return f"недопустимое значение для бинарного дерева: {self.new_val}," \
                    f"введите значение больше чем {self.root}"


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    # метод добавления левого потомка
    def insert_left(self, new_node):
        if new_node >= self.root:
            raise BinaryError(self.root, new_node, True, False)
        else:
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # метод добавления правого потомка
    def insert_right(self, new_node):
        if new_node <= self.root:
            raise BinaryError(self.root, new_node, False, True)
        else:
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(6)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())