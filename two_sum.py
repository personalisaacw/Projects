# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Assumed that each input would have exactly one solution, and may not use the same element twice.

def twoSum(nums, target):
    indices = {}  # create a dictionary to hold a number and it's index in nums

    for index, num in enumerate(nums):
        complement = target - num  # calculate the complement of the target and the current num

        if complement in indices:  # if the complement value is in the indicees dictionary
            return [indices.get(complement), index]  # return the index of the complement in the dictionary and the current index

        indices[num] = index
