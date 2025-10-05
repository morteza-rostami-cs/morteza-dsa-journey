
"""
# reverse a list in-place

# reverse a list -> using another list or other data structures

reversed = []

scores = [1, 2 ,3 , 4, 5, 6]

# two pointers 

"""

scores = [12, 13, 34, 34, 45, 3]

def reverse_list(arr: list[int]) -> None:
  """ reverse a list of int, in-place """

  left: int = 0 # first index 
  right: int = len(arr) - 1 # last index

  swap: int = 0

  while left < right:

    swap = arr[left]

    arr[left] = arr[right]
    arr[right] = swap

    # move our pointers
    left += 1
    right -= 1

reverse_list(arr=scores)

print(scores)

