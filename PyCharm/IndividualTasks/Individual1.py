#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Если список пуст, завершить программу.
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Найти сумму элементов кратных 2.
    new_A = [a for a in A if a % 2 == 0]

    print(f"Сумма элементов, кратных 2: {sum(new_A)}\n"
          f"Количество элементов, кратных 2: {len(new_A)}")
