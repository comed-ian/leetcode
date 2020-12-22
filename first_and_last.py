# Given a sorted array of integers, return the first and last
# indices of a target value in the array.  If none exist, return
# [-1, -1]

# Solution
# Time complexity: Worst case O(n) if two largest walls in middle
# Space complexity: O(1) - not using an auxiliary data struct

def first_and_last(arr, target): 
  return([binary_search(arr, target, "left"), binary_search(arr, target, "right")])

def binary_search(arr, target, mode):
  i = 0
  j = len(arr) - 1
  result = -1

  while (i <= j):
    mid = int((i + j) / 2)
    if (arr[mid] > target):
      j = mid - 1
    elif (arr[mid] < target):
      i = mid + 1
    else: 
      result = mid
      if (mode == 'left'):
        j = mid - 1
      else:
        i = mid + 1
  
  return result

def main(): 
  arr = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
  target = 6
  print("first and last indices: ", first_and_last(arr, target))

if __name__ == "__main__":
  main()