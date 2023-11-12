# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate(nums):
    sortedNums = sorted(nums)
    for i in range(0, len(sortedNums)):
        if i == len(sortedNums) - 1:
            return False
        elif sortedNums[i] == sortedNums[i + 1]:
            return True