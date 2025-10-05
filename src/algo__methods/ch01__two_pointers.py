"""

# what is two pointer method??

basically: 
- use two pointers -> p1 and p2 
to traverse through a data structure eg: array, string and so on.

# pointers can move:
  - in the same direction
  - away from each other 
  - or towards each other

  # we pick the direction -> based on the problem.

# common patterns of two pointers:
  # opposite ends -> towards each other
    - start p1 -> at the beginning, and start p2 at the end (right)
    move them inward -> until they meet.

  # same direction -> sliding window style
    both pointers -> start from the beginning -> p2 lags behind p1

  # different speeds -> fast & slow
    - p1 moves faster than p2

# PROBLEM:
============================

- ✅ Challenge 51: Reverse an array in-place

arr = [1, 2, 3, 4, 5, 6]




"""

# our list of numbers
numbers = [1, 2, 3, 4, 5, 6]

def reverse1(arr: list[int]) -> list[int]:
  """
  # reverse a list of int => by just looping from the end to start.

  """

  reversed: list[int] = []

  # start ->last index = length - 1
  # stop, 
  # step->count backwards
  for i in range(len(arr) - 1, -1, -1):
    reversed.append(arr[i])
    
  return reversed

# call reverse by looping from end
# res1 = reverse1(arr=numbers)
#print(f"result1: ", res1)

# reverse a list using two pointer method
# i should reversed in place -> meaning do not use another data structure, to push things into! eg: another array!

def reverse_two_pointers(nums: list[int]) -> None:
  """ reverse a list , in place! using two pointer method """

  left: int = 0 # first index
  right: int = len(nums) - 1 # starts with last index

  # use this -> to swap right with left
  swap: int = 0

  while True:
    #print(left , right)
    swap = nums[left] # hold the first element
    nums[left] = nums[right]
    
    nums[right] = swap # swap first one ->in last one

    # move your pointers
    right -= 1 # move left 
    left += 1 # move right
    
    # break the loop -> id pointers are equals
    """
    # even = [1, 2, 3, 4, 5, 6]
    """
    if left > right: # check if pointers are passed each other
      break # end

# reverse array in place
#reverse_two_pointers(nums=numbers)

#print(f"numbers after in place swap\n")
#print(numbers)

"""
# ✅ Challenge 52: Remove duplicates from a sorted array



"""

arr = [7, 3, 5, 3, 2, 8, 7, 9, 1, 5, 2, 6, 9, 4]

# sort this array

sorted_list = sorted(arr)
#print("sorted: ", sorted_list)

# remove duplicates using two pointers

def remove_duplicates(arr: list[int]) -> None:
  """ 
  remove duplicates or return unique values from a list
  #using two pointer method. 
  """

  last_unique = 0 # assume the first-index is a unique value
  # bound of our unique values which we put in front of list
  unique_bound = 1 # start with the index[1], after the first unique value

  # this pointer searches for unique values, also used to replace with unique_bound/a placeholder for the next unique value.
  scanner = 1 # start from index[1] also

  # loop once over the list
  while scanner < len(arr):

    # if we find a unique value
    if arr[last_unique] != arr[scanner]:

      # copy unique value into -> unique_bound
      arr[unique_bound] = arr[scanner]

      # increment unique bound
      unique_bound += 1

      # last index is always one less than unique bound
      last_unique = unique_bound - 1

    # we always move scanner forward -> regardless of finding a unique value or not
    scanner += 1

  # print the result 
  print('result: ', arr)

  # cut the list from end
  unique_values = arr[:unique_bound]
  print('unique values: \n')
  print(unique_values)

#remove_duplicates(arr=sorted_list)

"""
- ✅ Challenge 53: Container with most water (max area problem)


"""