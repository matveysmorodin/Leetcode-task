class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n =  len(nums)
        result = {}
        for i in range(n):
            if nums[i] not in result:
                result[nums[i]] = 1
            else:
                result[nums[i]] += 1
        return max(result, key = result.get)


'''
link: https://leetcode.com/problems/majority-element/?envType=problem-list-v2&envId=array

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

'''
