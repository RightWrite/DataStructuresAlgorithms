# Solution 1
# Time complexity O(n^2)
# Space complexity o(1)

def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# Solution 2
# Time complexity O(n)
# Space complexity O(n)
def twoNumberSum(array, targetSum):
    nums = set()
    for num in array:
        other_num = targetSum - num
        if other_num in nums:
            return [num, other_num]
        else:
            nums.add(num)
    return []


# Solution 3
# Time complexity O(n log(n))
# Space complexity O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left = left + 1
        else:
            right = right - 1
    return []
