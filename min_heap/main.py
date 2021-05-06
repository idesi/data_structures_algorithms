class Min_Heap:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def peek_min(self):
        return self._items[0] if self._items else None

    def insert(self, value):
        self._items.append(value)
        self.bubble_up(len(self._items) - 1)

    def extract_min(self):
        if len(self._items) == 0:
            return None

        last = self._items.pop()
        if len(self._items) == 0:
            return last

        min = self._items[0]
        self._items[0] = last
        self.bubble_down(0)

        return min

    def bubble_up(self, index):
        parentIndex = self.find_parent(index)
        if parentIndex is None:
            return

        parentValue = self._items[parentIndex]
        value = self._items[index]

        if parentValue < value:
            return

        self._items[parentIndex] = value
        self._items[index] = parentValue

        self.bubble_up(parentIndex)

    def find_parent(self, index):
        if index == 0:
            return None

        if index < 3:
            return 0

        return (index - 1) // 2

    def bubble_down(self, index):
        smaller_child, smaller_child_index = self.get_smaller_child(index)

        if smaller_child is None:
            return

        value = self._items[index]

        if smaller_child < value:
            self._items[smaller_child_index] = value
            self._items[index] = smaller_child
            return self.bubble_down(smaller_child_index)

    def get_children_indices(self, index):
        base = 0
        if index > 0:
            base = 2 * index

        return (base + 1, base + 2)

    def get_smaller_child(self, index):
        left_child_index, right_child_index = self.get_children_indices(index)
        left_child = (
            None
            if left_child_index + 1 > len(self._items)
            else self._items[left_child_index]
        )
        right_child = (
            None
            if right_child_index + 1 > len(self._items)
            else self._items[right_child_index]
        )

        if left_child is None and right_child is None:
            return (None, None)

        if left_child is None and right_child is not None:
            return (right_child, right_child_index)

        if right_child is None and left_child is not None:
            return (left_child, left_child_index)

        return (
            (left_child, left_child_index)
            if left_child < right_child
            else (right_child, right_child_index)
        )
