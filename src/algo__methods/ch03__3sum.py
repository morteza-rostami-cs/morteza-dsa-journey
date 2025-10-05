""""

Got it 👍 You don’t want the solution itself, just a **full problem description** like a coding challenge statement. Here’s one for **Challenge 54: 3Sum / 3Sum Closest** with clear constraints, input/output, and explanation:

---

# ✅ Challenge 54: 3Sum / 3Sum Closest

## Problem Description

You are given an array of integers `nums` and an integer `target`. Your task is to find three integers in `nums` such that their sum is **closest** to `target`.

* Return the sum of the three integers.
* You may assume that each input would have exactly one solution.

### Example 1

**Input:**

```
nums = [-1, 2, 1, -4], target = 1
```

**Output:**

```
2
```

**Explanation:**
The sum that is closest to the target is `(-1 + 2 + 1) = 2`.

---

### Example 2

**Input:**

```
nums = [0, 0, 0], target = 1
```

**Output:**

```
0
```

**Explanation:**
The only possible sum is `0 + 0 + 0 = 0`.

---

## Constraints

* `3 <= nums.length <= 500`
* `-10^3 <= nums[i] <= 10^3`
* `-10^4 <= target <= 10^4`

---

## Notes

* The problem is a variation of the **3Sum** problem.
* Unlike the standard 3Sum (which finds triplets that sum to exactly zero), here you are required to return the **closest possible sum** to the given target.
* Efficient solutions generally use **sorting + two pointers** to reduce time complexity from O(n³) (brute force) to O(n²).

---

Do you also want me to write a **separate problem description for the standard 3Sum (sum to zero)**, so you have both versions clear for your challenge list?


"""

"""

# given : an list of int 
nums = [-1, 2, 1, -4]

# and a target
target = 2

# find 3 integers => their sum closest to -> target

# return the sum of 3 int

# do not care -> if: multiple triplet -> that work! just return the first solution you find

# constraints:

# 3 <= nums.length <= 500

  # return: if array has less than 3 elements
  # and there is also some max limit -> for other reasons, does not matter

# -10^3 <= nums[i] <= 10^3

  # some limit for values of our list, that does not cause overflow
  # our sum has to be between -> -3000 and +3000

# -10^4 <= target <= 10^4

  # limit for target

"""

nums = [-1, 2, 1, -4]
# [-4, -1, 1, 2]

# list has to be sorted
# if sorted -> moving a pointer right increases total and moving left decreases the value
sorted_values = sorted(nums)

def find_closest_3sum(nums: list[int], target: int) -> int | None:

  # closest value to target
  closest = nums[0] + nums[1] + nums[len(nums) - 1] # assume the sum of first 3 values are closer to target

  # min distance to the target found
  min_distance = abs(closest - target) # -2 - 8

  # outer loop
  for i in range(len(nums)):
    # stop-> [i, x, x] ->cause: i greater than that and there are no 3 numbers to combine
    if i >= len(nums) - 2:
      break

    fixed = nums[i] # fixed in one outer loop

    # reset back pointers -> on start of each outer_loop
    left = i + 1 # always one more than fixed value
    right = len(nums) - 1 # start at the end

    # inner loop
    while True:
      
      # break if to pointers meet in the middle
      # break event if pointers are equal, cause: we need triple numbers not two
      if left >= right:
        break

      # initial closest sum
      sum3 = fixed + nums[left] + nums[right]

      # keep track of the closest
      distance = abs(sum3 - target)
      
      if distance < min_distance:
        # set new closest sum
        closest = sum3
        #set closets distance
        min_distance = distance

      print(f"i: {i}, f: {fixed} left: {left}, sum: {sum3}, right: {right}")
      
      # if: we found the exact target return
      if (sum3 == target):
        return sum3
      
      # if: under target -> move left
      if sum3 < target:
        left += 1

      elif sum3 > target:
        right -= 1 # decrease the total

  # return the closest
  return closest

# target = find_closest_3sum(nums=sorted_values, target=2)
# print(target)

print(find_closest_3sum(nums=sorted([3, -2, 5, 7, 1, -6, 4]), target=8))
print('\n\n\n')
print(find_closest_3sum(nums=sorted([10, -4, 2, -7, 3, 9, -1, 6]), target=-5))
  