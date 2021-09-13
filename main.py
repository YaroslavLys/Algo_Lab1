from algorithms.heapsort import HeapSort

if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    order = input()
    manager = HeapSort()
    print("Sorted array is")
    print(manager.heapsort(arr, order))
