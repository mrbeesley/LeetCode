from typing import List

'''
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).


    Example 1:

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    Example 2:

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    median_value = None
    combined_list = nums1 + nums2
    n_value = len(combined_list)
    if n_value == 0:
        return 0
    
    middle_value = int(n_value / 2)
    print(f'middle_value: {middle_value}')
    
    combined_list.sort()
    if n_value % 2 == 0:
        top_value = combined_list[int((n_value) / 2)]
        bottom_value = combined_list[int((n_value - 1) / 2)]
        median_value = (top_value + bottom_value) / 2
    else: 
        print(combined_list)
        median_position = int(n_value / 2)
        print(f'n value for odd: {median_position}')
        median_value = combined_list[median_position]
        
    return median_value


print(f'answer for input: nums1 = [1,3], nums2 = [2]')
print(findMedianSortedArrays([1,3], [2]))

print(f'answer for input: nums1 = [1,2], nums2 = [3,4]')
print(findMedianSortedArrays([1,2], [3,4]))

print(f'answer for input: nums1 = [8, 10, 12, 14, 1, 4, 6, 7, 3], nums2 = [10, 100, 30, 2, 5, 6, 76, 75, 12, 4]')
print(findMedianSortedArrays([8, 10, 12, 14, 1, 4, 6, 7, 3], [10, 100, 30, 2, 5, 6, 76, 75, 12, 4]))
    
print(f'answer for input: nums1 = [1,2], nums2 = []')
print(findMedianSortedArrays([1,2], []))

print(f'answer for input: nums1 = [], nums2 = []')
print(findMedianSortedArrays([], []))
    
