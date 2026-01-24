
#failed
def nextPermutation(nums) -> None:
    flag = 0
    print(-len(nums)+1)
    for i in range(-1,-len(nums),-1):
        if nums[i] > nums[i-1]:
            flag = 1
            tmp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = tmp  
            break
                      
    if flag == 0:
        nums[:] = nums[::-1]
    
nums = [1,3,2]
nextPermutation(nums)
print(nums)