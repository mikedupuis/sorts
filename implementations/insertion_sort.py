#!/usr/local/bin/python3

import argparse

from util.sort_util import SortableCollection

def get_sortable_collection():
    return SortableCollection([5, 1, 4, 2, 8])

def process_args():
    pass

def sort(sortable_collection):
    length = len(sortable_collection.data)
    for i in range(1, length):
        item_index = i

        for j in range(i - 1, -1, -1):
            if sortable_collection.compare(item_index, j) < 0:
                sortable_collection.swap(item_index, j)
                item_index -= 1
            else:
                break

    return sortable_collection
    
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

