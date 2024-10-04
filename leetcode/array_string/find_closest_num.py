
def findClosestNumber(nums):

    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
    return abs(closest) if closest < 0 and abs(closest) in nums else closest

findClosestNumber([2, 3,-1, 1, 8])
