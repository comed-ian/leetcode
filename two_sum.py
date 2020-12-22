# Given array of integers (no particular order) and a target value
# Return the array indices of a pair of numbers that sum to the target
# Cannot return the same pair twice in reverse order
# E.g. for [1, 2, 3, 4], target 4, can output:
# [0, 2] or [2, 0] but not both 

# Solution
# Time complexity: Worst case O(n) using hashmap
# Space complexity: Worst case O(n) for hashmap

def two_sum(arr, target):

  Dict = {}   # Define empty hashmap (dictionary) 
  for i in range(len(arr)):     # Iterate through array

    if (Dict.get(arr[i]) != None):      #
      return ([Dict.get(arr[i]), i])
    Dict[target - arr[i]] = i 


def main(): 
  arr = [4,2,3,1]
  target = 4

  print(two_sum(arr, target))

main()