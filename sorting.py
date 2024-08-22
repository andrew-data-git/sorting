"""
To be called by main and handle functions running the three sorting algorithms.
"""

import time


def sorting(numbers, algorithm):
    # https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running

    # TODO show the plot the graph

    return sort(numbers, algorithm)


def sort(numbers, algorithm):
    """
    A function that calls a sorting algorithm and runs it on given numbers

    Parameters
    ----------
    numbers : list
        List of numbers to be sorted.
    algorithm : int
        Name of sorting method to call.

    Returns
    -------
    A called function from user selection, and in practice a list of sorted numbers.
    """

    # start clock and print time to the terminal
    start_time = time.time()

    labels = {1: "Bubble",
                  2: "Insertion",
                  3: "Selection"}
    print(f"Running {labels[algorithm]} sort ...")
    algorithms = {1: bubble(numbers),
                  2: insertion(numbers),
                  3: selection(numbers)}

    # end clock
    print("--- Sorting took %s seconds ---" % (time.time() - start_time))

    return algorithms[algorithm]


def bubble(numbers):
    """
    Performs the bubble sort algorithm on a set of input numbers.
    https://www.javatpoint.com/daa-bubble-sort

    Parameters
    ----------
    numbers : list
        List of elements to be sorted.

    Returns
    -------
    numbers : list
        Sorted list of numbers.
    """
    n = len(numbers)
    swapped = True

    for i in range(n):
        if not swapped:
                return
        swapped = False

        for j in range(0, n-i-1):
            if numbers[i] > numbers[i+1]:
                numbers[i] = numbers[i+1]  # exchange numbers

                swapped = True
            # return numbers
            yield numbers

def insertion(numbers):
    """
    Performs the insertion sort algorithm on a set of input numbers.
    https://www.javatpoint.com/daa-insertion-sort

    Parameters
    ----------
    numbers : list
        List of elements to be sorted.

    Returns
    -------
    numbers : list
        Sorted list of numbers.
    """
    n = len(numbers)

    for i in range(1, n):  # start at second number
        key = numbers[i]
        j = i-1  # index of previous number
        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key

    return numbers


def selection(numbers):
    """
    Performs the selection sort algorithm on a set of input numbers.
    https://www.javatpoint.com/daa-selection-sort

    Parameters
    ----------
    numbers : list
        List of elements to be sorted.

    Returns
    -------
    numbers : list
        Sorted list of numbers.
    """
    n = len(numbers)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers
