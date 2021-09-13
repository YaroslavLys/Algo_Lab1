import unittest
from algorithms.heapsort import HeapSort


class TestHeapSort(unittest.TestCase):

    def test_sort(self):
        arr = [5, 4, 6, 1, 2, 3]
        manager = HeapSort()
        self.assertEqual(manager.heapsort(arr, "asc"), [1, 2, 3, 4, 5, 6])

    def test_desc_to_asc(self):
        arr = [6, 5, 4, 3, 2, 1]
        manager = HeapSort()
        self.assertEqual(manager.heapsort(arr, "asc"), [1, 2, 3, 4, 5, 6])

    def test_desc_to_desc(self):
        arr = [6, 5, 4, 3, 2, 1]
        manager = HeapSort()
        self.assertEqual(manager.heapsort(arr, "desc"), [6, 5, 4, 3, 2, 1])

    def test_asc_to_desc(self):
        arr = [1, 2, 3, 4, 5, 6]
        manager = HeapSort()
        self.assertEqual(manager.heapsort(arr, "desc"), [6, 5, 4, 3, 2, 1])

    def test_asc_to_asc(self):
        arr = [1, 2, 3, 4, 5, 6]
        manager = HeapSort()
        self.assertEqual(manager.heapsort(arr, "asc"), [1, 2, 3, 4, 5, 6])
