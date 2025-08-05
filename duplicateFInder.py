def find_duplicates(lst):
    freq = {}
    duplicates = []

    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, count in freq.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

# Example usage
nums = [4, 2, 7, 2, 3, 4, 8, 4]
print("Duplicate numbers:", find_duplicates(nums))
