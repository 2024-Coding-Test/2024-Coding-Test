import sys

while True:
    nums = list(map(int, sys.stdin.readline().strip().split()))

    if nums[0]==nums[1]==nums[2]== 0:
        break
    
    nums.sort() 
    
    if nums[2] >= sum(nums[:2]):
        print("Invalid")
    elif nums[0]==nums[1]==nums[2]:
        print("Equilateral")
    elif nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]:
        print("Isosceles")
    else:
        print("Scalene")