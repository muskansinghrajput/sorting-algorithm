
import random as rd

def bubbleSort(nums):
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
nums=[]
for i in range(1000):
    nums.append(rd.randint(10,90))

bubbleSort(nums)
print(nums)

n=int(input("Enter the element to search:"))
if n in nums:
    print(nums.index(n))
else:
    print("Not Found")
print("Inorder Traversal of the Binary Search Tree is :",nums)

