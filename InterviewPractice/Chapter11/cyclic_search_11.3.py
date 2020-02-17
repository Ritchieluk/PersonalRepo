def search_smallest(A)->int:
    left, right = 0, len(A)-1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid+1
        else:
            right = mid
    return left

arr = [378, 478, 550, 631, 102, 203, 220, 234, 279, 368]
arr1 = [402,403,405,412,430,520,560,8]
print(search_smallest(arr1))
