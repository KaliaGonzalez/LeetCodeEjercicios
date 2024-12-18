from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:   
    for i in nums1: 
        if(nums1[i]==0): 
            nums1.remove(i)  
    for j in nums2: 
        if(nums2[j] == 0): 
            nums2.remove(j)
    if(n == 0): 
        nums1 = nums1
    if (m == 0): 
        nums1 = nums1.extend(nums2)  
    nums1 = nums1 + nums2  
nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6] 
m = 3 
n = 3
merge(nums1,m,nums2,n)
print(nums1)