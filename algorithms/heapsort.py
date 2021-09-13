from timeit import default_timer as timer
from datetime import timedelta


class HeapSort:

    def __init__(self, swap_count=0, comparison_count=0):
        self.swap_count = swap_count
        self.comparison_count = comparison_count

    def heapsort(self, arr, order: str):
        self.sorting_start_time = timer()
        self.heapsort_helper(arr, order)
        self.sorting_end_time = timer()

        print('\n - Heap Sort - \n')
        print(f'execution time {timedelta(seconds=self.sorting_end_time - self.sorting_start_time)}')
        print(f'Swaps: {self.swap_count} ')
        print(f'Comparisons: {self.comparison_count} \n')
        return arr

    def heapsort_helper(self, arr, order: str):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i, order)

        for i in range(n - 1, 0, -1):
            self.swap_count += 1
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0, order)

    def heapify(self, arr, n, i, order: str):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        self.comparison_count += 1
        if order == "asc":
            if l < n and arr[i] < arr[l]:
                largest = l
        else:
            if l < n and arr[i] > arr[l]:
                largest = l

        self.comparison_count += 1
        if order == "asc":
            if r < n and arr[largest] < arr[r]:
                largest = r
        else:
            if r < n and arr[largest] > arr[r]:
                largest = r

        self.comparison_count += 1
        if largest != i:
            self.swap_count += 1
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapify(arr, n, largest, order)
