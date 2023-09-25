from abc import ABC, abstractmethod

"""Module with the base implementation of a Sort class."""

class Sort(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time
    
"""Module with the implementation of the BubbleSort algorithm."""

class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self):
        try:
            n = len(self._items)
            for i in range(n):
                for j in range(0, n-i-1): #iterating through every bubble of two consecutive items
                    if self._items[j] > self._items[j+1]: # comparing two items if greater first then swapping them
                        self._items[j], self._items[j+1] = self._items[j+1], self._items[j]
            return self._items
        except Exception as E: # error handling
            print(f"An error occured: {E}")
            return None
    
    def _time(self, items):
        # your code here

        return self.time

"""Module with the implementation of the MergeSort algorithm."""

class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self, items):
        # your code here

        return sorted_items

    def _merge(self, left, right):
        # your code here

        return merged

    def _time(self, items):
        # your code here

        return self.time