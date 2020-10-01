#!/usr/local/bin/python3

class SortableCollection:
    data = []
    swap_count = 0
    comparison_count = 0

    def __init__(data):
        self.data = data

    def is_sorted():
        minimum = data[0]
        length = len(data)

        for i in range(length):
            if data[i] < minimum:
                return False
            minimum = data[i]

        return True

    def _increment_swap_count():
        self.swap_count += 1

    def _increment_comparison_count():
        self.comparison_count += 1

    def compare(i, j):
        _increment_comparison_count()
        return data[i] - data[j]

    def swap(i, j):
        temp = data[i]
        data[i] = data[j]
        data[j] = temp
        _increment_swap_count()
