""""
#Merge Sort
def mergeSort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    # Merge elements one by one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining from left
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining from right
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Test case
arr = [4, 3, 2, 1, 5]
print(mergeSort(arr))  # Output: [1, 2, 3, 4, 5]
"""


def countInversions(arr):
    def mergesort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = mergesort(arr[:mid])
        right, inv_right = mergesort(arr[mid:])
        merged, inv_merge = merge_and_count(left, right)

        total_inversions = inv_left + inv_right + inv_merge
        return merged, total_inversions

    def merge_and_count(left, right):
        result = []
        i = j = 0
        inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv_count += len(left) - i  # All remaining elements in left are greater
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result, inv_count

    _, total = mergesort(arr)
    return total
