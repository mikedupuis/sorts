#!/usr/local/bin/python3

import argparse

from util.sort_util import SortableCollection

def get_sortable_collection():
    return SortableCollection([5, 1, 4, 2, 8])

def process_args():
    pass

def sort(collection: list) -> list:

    def merge(left: list, right: list) -> list:

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(sort(collection[:mid]), sort(collection[mid:]))

def main():
    process_args()

    unsorted_sortable_collection = get_sortable_collection()
    print("Sorting: {}".format(unsorted_sortable_collection.data))

    sorted_sortable_collection = sort(unsorted_sortable_collection)
    print("Sorted: {}".format(sorted_sortable_collection.data))
    print("Compare count: {}".format(sorted_sortable_collection.get_comparison_count()))
    print("Swap count: {}".format(sorted_sortable_collection.get_swap_count()))

if __name__ == '__main__':
    main()