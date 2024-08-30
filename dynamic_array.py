from typing import List, Optional, Iterator, Final
import array 

class DynamicArray:
  DEFAULT_CAPACITY: Final[int] = 8
  
  def __init__(self, array_capacity: Optional[int] = None) -> None:
    if array_capacity is None:
      array_capacity = self.DEFAULT_CAPACITY
    if array_capacity < 0:
      raise ValueError(f"Illegal Capacity: {array_capacity}")
  
    self.array_capacity = array_capacity
    self.static_array   = array.array('i', [0] * array_capacity)
    self.user_len       = 0
    
  @classmethod
  def from_list(cls, lst:Optional[List[int]]) -> 'DynamicArray':
    if lst is None:
      raise ValueError("List cannot be None")
    
    obj = cls(len(lst))
    obj.static_array   = array.array('i',lst)
    obj.user_len       = len(lst)
    obj.array_capacity = len(lst)
    return obj
  
  def size(self) -> int:
    return self.user_len
  

  def is_empty(self) -> bool:
    return self.user_len == 0
  

  def __getitem__(self, index: int) -> int:
    if 0 <= index < self.user_len:
      return self.static_array[index]
    
    raise IndexError("Index out of range") 


  def __setitem__(self, index: int, value: int) -> None:
    if 0 <= index < self.user_len:
      self.static_array[index] = value

    raise IndexError("Index out of range") 

  
  def add_element(self, elem: int) -> None:
    if self.user_len >= self.array_capacity:
      self._resize(max(1, self.array_capacity * 2))

    self.static_array[self.user_len] = elem
    self.user_len += 1


  def _resize(self, new_capacity: int) -> None:
    new_array = array.array('i', [0] * new_capacity)
    new_array[:self.user_len] = self.static_array[:self.user_len]
    self.static_array   = new_array
    self.array_capacity = new_capacity

  def remove_index(self,rm_index: int) -> None:
    if 0 <= rm_index < self.user_len:
      self.static_array[rm_index:-1] = self.static_array[rm_index+1:]
      self.user_len -= 1
      self.array_capacity -= 1

    raise IndexError("Index out of range") 
  

  def remove_element(self, elem: int) -> bool:
    for i in range(self.user_len):
      if self.static_array[i] == elem:
        self.remove_index(i)
        return True
    return False
  

  def reverse(self) -> None:
    for i in range(self.user_len // 2):
      self.static_array[i], self.static_array[self.user_len - i - 1] = \
        self.static_array[self.user_len - i - 1], self.static_array[i]
      

  def binary_search(self, key: int) -> None:
    left, right = 0, self.user_len -1

    while left <= right:
      mid = (left + right) // 2
      if self.static_array[mid] == key:
        return mid
      elif self.static_array[mid] < key:
        left = mid + 1
      else:
        right = mid - 1

    return -1
  

  def sort(self) -> None:
    self.static_array[:self.user_len] = array.array('i', sorted(self.static_array[:self.user_len]))

  def __iter__(self) -> Iterator[int]:
    return iter(self.static_array[:self.user_len])
  
  def __str__(self) -> str:
    return str(self.static_array[:self.user_len].tolist())
  
  def __repr__(self) -> str:
    return self.__str__()
  

if __name__ == "__main__":
  arr = DynamicArray(50)
  arr.add_element(3)
  arr.add_element(99)
  arr.add_element(278)
  arr.add_element(-14)

  for i in range(arr.size()):
    print(arr[i])

  arr.sort()

  print(arr)
