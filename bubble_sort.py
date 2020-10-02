#!/usr/local/bin/python3

import argparse

from util.sort_util import SortableCollection

def get_sortable_collection():
    return SortableCollection([5, 1, 4, 2, 8])

def process_args():
    pass
    #parser = argparse.ArgumentParser() 

    #parser.add_argument("input-file", help="file to sort")

    #args = parser.parse_args()
    #return GenerationConfig(int(args.count), int(args.max), int(args.min)) 

def compare(data, i, j):
    print("Comparing {} and {}".format(data[i], data[j]))
    increment_compare_count()
    return data[i] - data[j]

def swap(data, i, j):
    print("Swapping {} and {}".format(data[i], data[j]))
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    increment_swap_count()

def sort(sortable_collection):

    length = len(sortable_collection.data)

    sorted = False
    iteration = 0
    while not sorted:
        iteration += 1
        print("Iteration {}".format(iteration))
        sorted = True
        for i in range(length - 1):
            j = i + 1
            if sortable_collection.compare(i, j) > 0:
                sortable_collection.swap(i, j)
                sorted = False
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
