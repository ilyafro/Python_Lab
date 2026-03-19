class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # начало очереди (голова)
        self.end = None  # конец очереди (хвост)

    def pop(self):
        """
        Возвращаем элемент из начала очереди с удалением.
        """
        if self.start is None:
            raise Exception("Очередь пуста")

        val = self.start.data

        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None

        return val

    def push(self, val):
        """
        Добавление элемента в конец очереди.
        """
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n (нумерация с 0).
        """

        current = self.start
        index = 0
        while current is not None and index < n:
            current = current.nref
            index += 1

        new_node = Node(val)

        if current == self.start:
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
        elif current is None:
            if self.end:
                self.end.nref = new_node
                new_node.pref = self.end
                self.end = new_node
            else:
                self.start = new_node
                self.end = new_node
        else:
            prev_node = current.pref
            new_node.pref = prev_node
            new_node.nref = current
            prev_node.nref = new_node
            current.pref = new_node

    def print(self):
        """
        Вывод содержимого очереди от начала к концу.
        """
        current = self.start
        while current is not None:
            print(current.data)
            current = current.nref