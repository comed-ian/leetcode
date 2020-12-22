
class Solution(object):
    def moveZeroes(self, nums):
        front = 0
        back = 0
        while (front < len(nums)):
            if (nums[back] != 0): 
              back += 1
              continue
            elif (front <= back):
              front = back + 1
            if (nums[front] != 0):
              nums[front], nums[back] = nums[back], nums[front]
              back += 1
              continue
            front += 1
        return nums

def main():
  arr = [0,1,0,3,0]
  test = Solution()
  print (test.moveZeroes(arr))

main()
