
"""

Here’s a clean problem description for **Challenge 55: Maximum Sum Subarray of Size K**:

---

## Challenge 55: Maximum Sum Subarray of Size K ✅

### Problem Description

Given an array of **integers** and a number `k`, find the **maximum sum of any contiguous subarray of size `k`**.

You need to implement a function that efficiently computes this maximum sum using the **sliding window technique**.

---

### Function Signature (JavaScript)

```js
/**
 * Returns the maximum sum of any contiguous subarray of size k.
 * @param {number[]} arr - The input array of integers
 * @param {number} k - The size of the subarray
 * @returns {number} - Maximum sum of any contiguous subarray of size k
 */
function maxSubarraySum(arr, k) {
  // your code here
}
```

---

### Input

* `arr` — an array of integers, e.g., `[2, 1, 5, 1, 3, 2]`
* `k` — a positive integer, representing the size of the subarray, e.g., `3`

Constraints:

* `1 <= k <= arr.length`
* Array can contain positive or negative integers.

---

### Output

* A single integer — the **maximum sum** of any contiguous subarray of size `k`.

---

### Example 1

**Input:**

```js
arr = [2, 1, 5, 1, 3, 2]
k = 3
```

**Output:**

```
9
```

**Explanation:**
The subarray `[5, 1, 3]` has the maximum sum of `9`.

---

### Example 2

**Input:**

```js
arr = [2, 3, 4, 1, 5]
k = 2
```

**Output:**

```
7
```

**Explanation:**
The subarray `[3, 4]` has the maximum sum of `7`.

---

### Notes

* This problem is ideal for the **sliding window** pattern.
* The naive solution checks all subarrays of size `k` (O(n × k)), but sliding window achieves **O(n) time**.

---



"""

"""

# what is sliding window?



"""

# naive solution
def max_subarray_sum_naive(arr: list[int], k: int) -> float | None:
  """ naive solution to problem: find the max sum of k , consecutive numbers in an array """

  # array length
  length: int = len(arr)

  # k can't be smaller than array length -> 3 elements in array of 2 does not mean anything
  if k > length:
    return None
  
  # take -infinity as our initial max 
  max_sum = float("-inf")

  # then outer loop 
  # if: k = 3 -> i = 0, 1, 2, 3 -> think we are moving a window with 3 elements
  for i in range(length - k + 1): # type: ignore
    
    # current sum of k elements
    current_sum = 0

    # inner loop -> add eah 3 elements
    for j in range(i, i + k): # 3, 3+3=6 -> 3, 4, 5
      current_sum += arr[j]
    
    # if we found a new max
    max_sum = max(max_sum, current_sum) # set the bigger one

  return max_sum


arr = [2, 1, 5, 1, 3, 2]

k = 3

# maximum: float | None = max_subarray_sum_naive(arr=arr, k=k)

# print(maximum)

#===============================

# sliding window solution

#        . 
# arr = [2, 1, 5, 1, 3, 2]
 
def slide_window(arr: list[int], k: int) -> float | None:

  # length of array
  length = len(arr)

  # length <= k
  if k > length:
    print("k is bigger than length")
    return None
  
  left = 0
  right = 0
  # [1, 2, 3] k = 3
  # right has to be end of window -> 3 - 1 = 2 ->eg: 0, 1, 2
  window = left + k - 1

  max_sum = float('-inf')
  current_max = 0
  
  while True:
    if right >= length or window >= length:
      print("right pointer out of bound")
      #return right
      break

    # gather each window values
    current_max += arr[right]

    print(left, right, arr[right])

    right += 1
    
    if right > window:
      print(f"✅ window: {window}")

      # check for bigger max
      if current_max > max_sum:
        max_sum = current_max

      # reset current max -> for next window
      current_max = 0

      # move left
      left += 1

      # rest right to left
      right = left

      # reset window , relative to left
      window = left + k -1

  return max_sum

# [2, 1, 5, 1, 3, 2]
# print(slide_window(arr=arr, k=k))

def slide_window2(arr: list[int], k: int) -> float | None:

  # length of array
  length = len(arr)

  # length <= k
  if k > length:
    print("k is bigger than length")
    return None
  
  # the biggest we have found so far
  max_sum = 0
  #✅ sum of current window
  current_sum = 0
  
  # first loop: to sum the first k elements in list
  for i in range(k): # stop_index is not included
    current_sum += arr[i]

  # as we move window we sum
  max_sum = current_sum
  
  # second loops is to move window
  left = 0
  right = 0
  while True:

    # move left and right pointer
    left += 1
    right = left + k - 1

    # STOP
    if right >= length:
      print('right pointer out of bound')
      break

    # remove: old_left and add new right
    current_sum = current_sum - arr[left - 1] + arr[right] 

    #print(f"\n right: {right}, current: {current_sum} \n")

    if current_sum > max_sum:
      max_sum = current_sum

  return max_sum

# [2, 1, 5, 1, 3, 2]
print(slide_window2(arr=arr, k=k))