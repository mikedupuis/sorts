#!/usr/local/bin/python3

class SortableCollection:
    data = []
    swap_count = 0
    comparison_count = 0

    def __init__(self, data):
        self.data = data

    def is_sorted():
        minimum = self.data[0]
        length = len(self.data)

        for i in range(length):
            if self.data[i] < minimum:
                return False
            minimum = self.data[i]

        return True

    def get_swap_count(self):
        return self.swap_count

    def get_comparison_count(self):
        return self.comparison_count

    def _increment_swap_count(self):
        self.swap_count += 1

    def _increment_comparison_count(self):
        self.comparison_count += 1

    def compare(self, i, j):
        self._increment_comparison_count()
        return self.data[i] - self.data[j]

    def swap(self, i, j):
        self._increment_swap_count()
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
