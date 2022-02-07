"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque
from json import dumps
from pympler import asizeof


class Huffman:

    def __init__(self, user_string):
        self.user_string = user_string
        self.code_table = dict()
        self.huffman_code(self.get_tree())

    def get_counter_symbol(self):
        return Counter(self.user_string)

    def sort_counter_value(self):
        return deque(sorted(self.get_counter_symbol().items(),
                            key=lambda item: item[1]))

    def get_tree(self):
        sort_value = self.sort_counter_value().copy()
        if len(sort_value) != 1:
            while len(sort_value) > 1:
                weight = sort_value[0][1] + sort_value[1][1]
                tree_dict = {0: sort_value.popleft()[0],
                            1: sort_value.popleft()[0]}
                for i, _count in enumerate(sort_value):
                    if weight > _count[1]:
                        continue
                    else:
                        sort_value.insert(i, (tree_dict, weight))
                        break
                else:
                    sort_value.append((tree_dict, weight))
        else:
            weight = sort_value[0][1]
            tree_dict = {0: sort_value.popleft()[0], 1: None}
            sort_value.append((tree_dict, weight))
        tree_dict = dumps(tree_dict)
        return sort_value[0][0]

    def huffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code(tree[0], path=f'{path}0')
            self.huffman_code(tree[1], path=f'{path}1')

    def get_string(self):
        result = ''
        for symbol in self.user_string:
            result += self.code_table[symbol]
        return result

    def decoding(self, code_string):
        res = ''
        i = 0
        codes_dict = self.code_table
        while i < len(code_string):
            for code in codes_dict:
                if code_string[i:].find(codes_dict[code]) == 0:
                    res += code
                    i += len(codes_dict[code])
        codes_dict = dumps(codes_dict)
        return res


user_input = input("Введите строку: ")
OBJ = Huffman(user_input)
TREE_OBJ = OBJ.get_tree()
code_str = OBJ.get_string()
print(f"Исходная строка: {user_input}\n")
print(f"Дерево: {TREE_OBJ}\n")
print(f"Таблица c кодами: {OBJ.code_table}\n")
print(f"Строка кода после кодирования: {code_str}\n")
print(f"Декодированная строка: {OBJ.decoding(code_str)}")

"""
Так как тема сложная и малопотянтная для меня, был взят за основу код примера с урока.

Словари были законсервированы, что привело к значительному снижению затрат памяти:
При вводе строки 'qaz', до консервации словаря tree_dict размер был - 688, стал 88.
При вводе той же строки, до консервации словаря code_table размер был 568, стал 88.
Были переименованы переменные и названия функций.
"""