# Given array of integers (SORTED) and a target value
# Return the array indices of a pair of numbers that sum to the target
# Cannot return the same pair twice in reverse order
# E.g. for [1, 2, 3, 4], target 4, can output:
# [0, 2] or [2, 0] but not both 
# Target space complexity O(1) 

# Solution
# Time complexity: Worst case O(n) if only two values straddle the median
# Space complexity: O(1) - only additional variables required 

def two_sum_two(arr, target):
  front = 0
  back = len(arr) - 1
  while front < back:
    if (arr[front] + arr[back] == target):
      return [front, back]
    elif (arr[front] + arr[back] < target):
      front += 1
    else: 
      back -= 1


def main(): 
  arr = [1,2,3,9]
  target = 11

  print(two_sum_two(arr, target))

main()