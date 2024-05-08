

def twoSum (self, nums, target):
    sums = []
    index1 = 0
    index2 = 1

    for num1 in nums:
        for num2 in range(1, len(nums)-1):
            if num1 + num2 == target:
                return [index1, index2]
            else:
                index2 = index2 + 1
            
        index1 = index1 + 1

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))