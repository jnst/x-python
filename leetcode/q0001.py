from typing import List


class Solution:
    @classmethod
    def two_sum(cls, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i >= j:
                    continue
                if (nums[i] + nums[j]) == target:
                    return [i, i+1]
        return []


class Test:
    def __init__(self, *, nums=None, target=None, expects=None):
        self.__nums = nums
        self.__target = target
        self.__expects = expects

    @property
    def nums(self):
        return self.__nums

    @property
    def target(self):
        return self.__target

    @property
    def expects(self):
        return self.__expects


if __name__ == '__main__':
    test_cases = [
        Test(nums=[2, 7, 11, 15], target=9, expects=[0, 1]),
        Test(nums=[2, 7, 11, 15], target=0, expects=[]),
        Test(nums=[2, 7, 11, 15], target=18, expects=[1, 2]),
    ]

    for case in test_cases:
        ans = Solution.two_sum(case.nums, case.target)
        assert ans == case.expects
