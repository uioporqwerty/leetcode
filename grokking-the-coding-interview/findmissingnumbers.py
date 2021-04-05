def find_missing_numbers(nums):
    missingNumbers = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if j < len(nums) and nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            missingNumbers.append(i + 1)

    return missingNumbers


print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_missing_numbers([2, 4, 1, 2]))
print(find_missing_numbers([2, 3, 2, 1]))
