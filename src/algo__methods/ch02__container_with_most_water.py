
"""
Absolutely! Let’s write a **detailed problem description** for the “Container With Most Water” challenge.

---

# ✅ Challenge 53: Container With Most Water (Max Area Problem)

## **Problem Description**

You are given an array of **non-negative integers** where each integer represents the **height of a vertical line** drawn at that index. The lines are drawn **at equal spacing along the x-axis**.

Your task is to **find two lines** that, together with the x-axis, form a container that **holds the most water**. You need to **return the maximum amount of water** that can be contained.

---

## **Input**

* An array of non-negative integers: `height = [h0, h1, h2, ..., hn-1]`
* Each element represents the height of a vertical line.
* The width between adjacent lines is 1 unit.

---

## **Output**

* An integer representing the **maximum water area** that can be formed between **any two lines**.

---

## **Constraints**

* `2 <= height.length <= 10^5`
* `0 <= height[i] <= 10^4`

---

## **Explanation / Example**

**Example 1:**

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

* The container with max water is formed by the lines at index 1 (height 8) and index 8 (height 7).
* Width = 8 - 1 = 7
* Height = min(8,7) = 7
* Area = width * height = 7 * 7 = 49

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

* Only two lines exist, so the area = 1 * 1 = 1

---

## **Hints / Notes**

* ✅ This is a **classic two-pointer problem**:

  * Place **one pointer at the start** and **one at the end** of the array.
  * Calculate the area for the lines at these two pointers.
  * Move the pointer pointing to the **smaller height** inward, because moving the taller one **cannot increase the area**.
  * Repeat until the two pointers meet.
* This **greedy approach** ensures you find the maximum area in **O(n) time** with **O(1) space**.

---

If you want, I can also **draw a small visual diagram** showing two pointers and the area calculation — it makes this problem super clear before coding.

Do you want me to do that?


"""

"""
# problem description:

# we have index and value -> in a list of heights

height = [1, 3, 2, 5, 4]

eg: 
index[1] => (1, 0) => each index represent a (x,y) point on 2d plane.

height[1] => (1, 3) or (index, value) => this is also your second point

# to gether they form a line -> a vertical line

# so each index has a vertical line:

    |
|   |
|   |
|   |
1---4

# so: you see index[1] has shorter height -> can holder less water!
# and we only care about the shorter side of the container.

# so
container height = min(height[1], height[4])
container width = distance on x-axis -> index[4] - index[1]

area = min(height[p1] - height[p2]) * (p2 - p1)

"""

height = [1, 3, 2, 5, 4]

def max_area_problem(heights: list[int]) -> int:

  # pointer one
  p1 = 0 # start from index[0]
  # pointer two
  p2 = len(heights) - 1 # start and end

  # area of container: 
  # area = min(height[p1] - height[p2]) * (p2 - p1)
  max_area = min(heights[p1], heights[p2]) * (p2 - p1) # init value , assume the first value is greatest area

  while p1 < p2: # pointers meet
    # calc the area
    new_area = min(heights[p1], heights[p2]) * (p2 - p1) # shorter_side * distance = area

    if new_area > max_area:
      max_area = new_area # only if we find a bigger area

    # move the pointer with smaller (line/height)
    if heights[p1] < heights[p2]:
      # move to right
      p1 += 1
    elif heights[p2] < heights[p1]:
      # move to left 
      p2 -= 1 # move the shorter line, keep other pointer on larger line
    else: # maybe equal height
      # move any of the pointers , does not matter, we don't miss the larger line
      p1 += 1

  return max_area

res1 = max_area_problem(heights=height)
print("res1 \n")
print(res1)
