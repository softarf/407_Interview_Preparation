# -*- coding: utf-8 -*-
#                       "Подготовка к собеседованию".
#                   Задача №1. Создать класс MyStack с заданными методами.
#                   Задача №2. Используя созданный класс, проверить набор скобок на сбалансированность.
#
from typing import List, Any

from modules import MyStack


def work_with_stack(set_brackets: str) -> str:
    """Проверяет последовательность скобок на сбалансированность."""
    OPENING_BRACKETS: List[str] = ['(', '[', '{']
    brackets_stack: Any = MyStack()
    result: str = ""
    bracket: str
    for bracket in set_brackets:
        if bracket in OPENING_BRACKETS:
            brackets_stack.push(bracket)
        elif (brackets_stack.size() > 0
              and (bracket == ')' and brackets_stack.peek() == '('
                   or bracket == ']' and brackets_stack.peek() == '['
                   or bracket == '}' and brackets_stack.peek() == '{')):
            brackets_stack.pop()
        else:
            result = "Несбалансированно."
            break
    if result == "" and brackets_stack.is_empty():
        result = "Сбалансированно."
    return result


def main():
    """Осуществляет подготовку исходных данных и вывод результата выполнения."""
    brackets_list: str = input('Задайте набор скобок: ')
    res: str = work_with_stack(brackets_list)
    print(res)


if __name__ == '__main__':
    main()
    # input('\n  -- Конец --  ')  # Типа  "Пауза" - Для среды
