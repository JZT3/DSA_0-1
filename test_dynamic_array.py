import unittest
import array
from typing import Optional, List
from dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):

    def test_initialization_default_capacity(self):
        """Test initialization with default capacity."""
        arr = DynamicArray()
        self.assertEqual(arr.size(), 0)
        self.assertEqual(arr.array_capacity, DynamicArray.DEFAULT_CAPACITY)
        self.assertEqual(arr.static_array.tolist(), [0] * DynamicArray.DEFAULT_CAPACITY)

    def test_initialization_with_custom_capacity(self):
        """Test initialization with a custom capacity."""
        custom_capacity = 20
        arr = DynamicArray(custom_capacity)
        self.assertEqual(arr.size(), 0)
        self.assertEqual(arr.array_capacity, custom_capacity)
        self.assertEqual(arr.static_array.tolist(), [0] * custom_capacity)

    def test_initialization_with_negative_capacity(self):
        """Test initialization with a negative capacity."""
        with self.assertRaises(ValueError):
            DynamicArray(-10)

    def test_add_element(self):
        """Test adding elements to the array."""
        arr = DynamicArray(2)
        arr.add_element(1)
        arr.add_element(2)
        self.assertEqual(arr.size(), 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
    
    def test_add_element_resize(self):
        """Test array resizing when adding elements beyond capacity."""
        arr = DynamicArray(2)
        arr.add_element(1)
        arr.add_element(2)
        arr.add_element(3)  # Should trigger a resize
        self.assertEqual(arr.size(), 3)
        self.assertEqual(arr.array_capacity, 4)
        self.assertEqual(arr[2], 3)
    
    def test_get_item(self):
        """Test retrieving elements using __getitem__."""
        arr = DynamicArray.from_list([1, 2, 3])
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)

    def test_get_item_out_of_bounds(self):
        """Test __getitem__ with an out-of-bounds index."""
        arr = DynamicArray.from_list([1, 2, 3])
        with self.assertRaises(IndexError):
            arr[3]

    def test_set_item(self):
        """Test setting elements using __setitem__."""
        arr = DynamicArray.from_list([1, 2, 3])
        arr[1] = 99
        self.assertEqual(arr[1], 99)
    
    def test_set_item_out_of_bounds(self):
        """Test __setitem__ with an out-of-bounds index."""
        arr = DynamicArray.from_list([1, 2, 3])
        with self.assertRaises(IndexError):
            arr[3] = 99

    def test_remove_index(self):
        """Test removing an element by index."""
        arr = DynamicArray.from_list([1, 2, 3])
        arr.remove_index(1)
        self.assertEqual(arr.size(), 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 3)

    def test_remove_index_out_of_bounds(self):
        """Test remove_index with an out-of-bounds index."""
        arr = DynamicArray.from_list([1, 2, 3])
        with self.assertRaises(IndexError):
            arr.remove_index(3)
    
    def test_remove_element(self):
        """Test removing an element by value."""
        arr = DynamicArray.from_list([1, 2, 3])
        result = arr.remove_element(2)
        self.assertTrue(result)
        self.assertEqual(arr.size(), 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 3)
    
    def test_remove_element_not_found(self):
        """Test remove_element with a value not in the array."""
        arr = DynamicArray.from_list([1, 2, 3])
        result = arr.remove_element(99)
        self.assertFalse(result)
        self.assertEqual(arr.size(), 3)
    
    def test_reverse(self):
        """Test reversing the array."""
        arr = DynamicArray.from_list([1, 2, 3, 4])
        arr.reverse()
        self.assertEqual(arr[0], 4)
        self.assertEqual(arr[1], 3)
        self.assertEqual(arr[2], 2)
        self.assertEqual(arr[3], 1)

    def test_reverse_empty_array(self):
        """Test reversing an empty array."""
        arr = DynamicArray()
        arr.reverse()
        self.assertEqual(arr.size(), 0)
    
    def test_binary_search_found(self):
        """Test binary search for an element that exists."""
        arr = DynamicArray.from_list([1, 2, 3, 4, 5])
        index = arr.binary_search(3)
        self.assertEqual(index, 2)

    def test_binary_search_not_found(self):
        """Test binary search for an element that doesn't exist."""
        arr = DynamicArray.from_list([1, 2, 3, 4, 5])
        index = arr.binary_search(99)
        self.assertEqual(index, -1)
    
    def test_sort(self):
        """Test sorting the array."""
        arr = DynamicArray.from_list([4, 3, 1, 2])
        arr.sort()
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 4)
    
    def test_str_and_repr(self):
        """Test __str__ and __repr__ methods."""
        arr = DynamicArray.from_list([1, 2, 3])
        self.assertEqual(str(arr), "[1, 2, 3]")
        self.assertEqual(repr(arr), "[1, 2, 3]")
    
    def test_is_empty(self):
        """Test the is_empty method."""
        arr = DynamicArray()
        self.assertTrue(arr.is_empty())
        arr.add_element(1)
        self.assertFalse(arr.is_empty())
    
    def test_from_list(self):
        """Test creating an array from a list."""
        lst = [1, 2, 3]
        arr = DynamicArray.from_list(lst)
        self.assertEqual(arr.size(), len(lst))
        self.assertEqual(arr.array_capacity, len(lst))
        for i in range(len(lst)):
            self.assertEqual(arr[i], lst[i])
    
    def test_iter(self):
        """Test the __iter__ method."""
        arr = DynamicArray.from_list([1, 2, 3])
        elements = list(arr)
        self.assertEqual(elements, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
