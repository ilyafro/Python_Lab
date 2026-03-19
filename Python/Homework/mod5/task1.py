class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека (фактически — вершину)

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            raise Exception("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка (на вершину стека)
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека (сверху вниз)
        """
        current = self.end
        while current is not None:
            print(current.data)
            current = current.pref