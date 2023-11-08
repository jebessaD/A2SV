class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m-1
        ptr2= n-1
        ind= m + n -1

        while ptr1 > -1 and ptr2 > -1:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ind],nums1[ptr1] = nums1[ptr1],nums1[ind]
                ptr1-=1
            else:
                nums1[ind] = nums2[ptr2]
                ptr2-=1
            ind -= 1
            
        if ptr1==-1:
            nums1[:ptr2 + 1] = nums2[:ptr2+1]