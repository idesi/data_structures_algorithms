import unittest
from main import Min_Heap


class MinHeapTestCase(unittest.TestCase):
    def test_min_heap_returns_None_if_peek_is_called_with_no_items(self):
        heap = Min_Heap()
        self.assertEqual(heap.peek_min(), None)

    def test_min_heap_returns_None_if_extract_is_called_with_no_items(self):
        heap = Min_Heap()
        self.assertEqual(heap.extract_min(), None)

    def test_min_heap_has_the_correct_root_when_an_item_is_added(self):
        heap = Min_Heap()
        heap.insert(20)
        self.assertEqual(heap.peek_min(), 20)

    def test_min_heap_has_the_correct_items_as_they_are_added(self):
        heap = Min_Heap()
        heap.insert(5)
        heap.insert(20)
        self.assertEqual(heap._items[0], 5)
        self.assertEqual(heap._items[1], 20)

    def test_min_heap_changes_the_root_if_smaller_item_is_added(self):
        heap = Min_Heap()
        heap.insert(20)
        heap.insert(5)
        self.assertEqual(heap.peek_min(), 5)

    def test_min_heap_does_not_rebalance_when_level_as_room_for_smaller_item(self):
        heap = Min_Heap()
        heap.insert(20)
        heap.insert(5)
        heap.insert(15)
        self.assertEqual(heap._items[0], 5)
        self.assertEqual(heap._items[1], 20)
        self.assertEqual(heap._items[2], 15)

    def test_min_heap_works_as_expected_as_more_levels_are_added(self):
        heap = Min_Heap()
        heap.insert(20)
        heap.insert(5)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        self.assertEqual(heap._items[0], 5)
        self.assertEqual(heap._items[1], 20)
        self.assertEqual(heap._items[2], 15)
        self.assertEqual(heap._items[3], 22)
        self.assertEqual(heap._items[4], 40)

    def test_min_heap_rebalances_and_bubbles_up_when_smaller_item_is_added(self):
        heap = Min_Heap()
        heap.insert(5)
        heap.insert(20)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        heap.insert(6)
        self.assertEqual(heap._items[0], 5)
        self.assertEqual(heap._items[1], 20)
        self.assertEqual(heap._items[2], 6)
        self.assertEqual(heap._items[3], 22)
        self.assertEqual(heap._items[4], 40)
        self.assertEqual(heap._items[5], 15)

    def test_min_heap_extracts_all_items_in_the_correct_order(self):
        mins = []
        heap = Min_Heap()
        heap.insert(5)
        heap.insert(20)
        heap.insert(15)
        heap.insert(3)
        heap.insert(22)
        heap.insert(40)
        heap.insert(6)

        while heap:
            mins.append(heap.extract_min())
        self.assertEqual(mins, [3, 5, 6, 15, 20, 22, 40])

    def test_min_heap_returns_the_correct_length(self):
        heap = Min_Heap()
        self.assertEqual(len(heap), 0)
        heap.insert(5)
        self.assertEqual(len(heap), 1)
        heap.insert(6)
        self.assertEqual(len(heap), 2)
        heap.extract_min()
        self.assertEqual(len(heap), 1)
        heap.extract_min()
        self.assertEqual(len(heap), 0)
        heap.extract_min()
        self.assertEqual(len(heap), 0)


if __name__ == "__main__":
    unittest.main()
