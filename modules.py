# -*- coding: utf-8 -*-
#                       "Подготовка к собеседованию".
#                   Класс к задаче №1. Создать класс MyStack с заданными методами.
#
from typing import List


class MyStack:
    """
    Абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO
    (англ. last in — first out, «последним пришёл — первым вышел»).
    """

    def __init__(self) -> None:
        """Создаёт стек."""
        self.stack: List[str] = list()

    def is_empty(self) -> bool:
        """Проверяет стек на пустоту."""
        if len(self.stack) > 0:
            return False
        return True

    def push(self, element: str) -> None:
        """Добавляет новый элемент на вершину стека."""
        self.stack.append(element)

    def pop(self) -> str:
        """Удаляет верхний элемент стека. Возвращает этот элемент."""
        return self.stack.pop()

    def peek(self) -> str:
        """Возвращает верхний элемент стека, но не удаляет его."""
        return self.stack[len(self.stack) - 1]

    def size(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self.stack)
