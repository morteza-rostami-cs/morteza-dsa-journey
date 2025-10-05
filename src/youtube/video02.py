"""
# ✅ Challenge 52: Remove duplicates from a sorted array

# two pointer method:

"""

arr = [7, 3, 5, 3, 2, 8, 7, 9, 1, 5, 2, 6, 9, 4]

sorted_arr = sorted(arr)

# [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
# print(sorted_arr)

def remove_duplicates(arr: list[int]) -> None:
  """
  # remove all duplicates or find and print unique values.
  # using two pointer method
  """

  # p1
  last_unique = 0 # first unique value

  # u
  unique_bound = 1

  # p2
  scanner = 1

  while scanner < len(arr):

    # p1 != p2
    if arr[last_unique] != arr[scanner]:
      arr[unique_bound] = arr[scanner] # unique value found

      # increment p1
      unique_bound += 1

      # last_unique = unique_bound - 1
      last_unique = unique_bound - 1

    # unique value found or not
    scanner += 1

  print('result after loop: ')
  print(arr)

  unique_values = arr[:unique_bound]
  print(unique_values)

remove_duplicates(arr=sorted_arr)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 8, 9, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""