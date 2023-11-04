#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(float, input().split()))
    # Если список пуст, завершить программу.
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    #Найти количество положительных элементов списка.
    positive_elements = list(filter(lambda x: x > 0, A))

    # Найти сумму элементов списка после последнего нуля.
    null_index = A[::-1].index(0)
    sum_after_null = sum(A[-null_index:])

    #Преобразовать список.
    small_A = list(filter(lambda x: x < 2, A))
    big_A = list(filter(lambda x: x >= 2, A))
    small_A.extend(big_A)

    print(f"Преобразованный список {small_A}")

