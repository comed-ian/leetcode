# Given array of integers (no particular order)
# The numbers correspond to the height of "walls", and their 
# indices are their location on the x-axis
# Return the maximum volume (area) that can be contained 
# between two walls in the set


# Solution
# Time complexity: Worst case O(n) if two largest walls in middle
# Space complexity: O(1) - not using an auxiliary data struct


def max_water(arr): 
  # Initialize two-pointers and max to return
  front = 0
  back = len(arr) - 1
  max = 0

  # Iterate from front and back. Volume is dependent on the
  # shorter of the two walls. While iterating, increment the
  # smaller of the two walls 
  while front != back:
    if ((back - front) * min([arr[back], arr[front]]) > max):
      max = (back - front) * min([arr[back], arr[front]])
    if (arr[front] < arr[back]):
      front += 1
    else:
      back -=1
  return max

def main():
  arr = [10, 5, 2, 6, 10]
  print ("max volume: ", max_water(arr))

main()