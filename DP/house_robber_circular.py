# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

def house_robber(nums):
    rob1, rob2 =0, 0 
    for i in nums:
        temp = max(i + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
def house_robber_circular(nums):
    #split the houses into two scenarios:
    #1. Rob houses from index 0 to n-2 (exclude the last house)
    #2. Rob houses from index 1 to n-1 (exclude the first house)
    houses1 = nums[:-1]
    houses2 = nums[1:]
    return max(house_robber(houses1), house_robber(houses2))