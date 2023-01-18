def twoSum(nums, target):
    result = []
    found = False
    for i in range(0, len(nums)):
        for j in (0, len(nums)-1):
            if nums[i]+nums[j] == target:
                if i == 0 and j == 0 :
                    pass
                elif found == True:
                    pass
                else:
                    found = True
                    result.append(i)
                    result.append(j)   
    return result   
print(twoSum([2,5,5,11], 10))