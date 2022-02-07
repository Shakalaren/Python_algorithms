"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""

check = False


class OwnError(Exception):
    pass

class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if new_node > self.root:
                raise OwnError
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except OwnError:
            print('Введено неверное значение для левого потомка. Требования дерева не выполнены')

    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise OwnError
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except OwnError:
            print('Введено неверное значение для правого потомка. Требования дерева не выполнены')

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_val(self):
        return self.root



r = BinaryTree(13)
r.insert_left(12)
r.insert_right(15)
r.get_root_val()
r.get_left_child()
r.insert_left(10)
r.insert_right(13)
r.get_root_val()
r.get_right_child()
r.insert_left(13)
r.insert_right(16)