def f_duplicates(nums):
    a = set()
    duplicate = set()
    
    for num in nums:
        if num in a:
            duplicate.add(num)
        else:
            a.add(num)
    
    return list(duplicate)


nums = [4, 2, 3, 4, 5, 2, 7, 3, 9]

result = f_duplicates(nums)
print("Duplicate numbers:", result)
