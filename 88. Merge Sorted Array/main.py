class Solution:
    def merge(self, nums1: List[int], p1: int, nums2: List[int], p2: int) -> None:
        i = p1 + p2 -1
        p1-=1
        p2-=1
        while p2 >= 0:
            if nums2[p2] >= nums1[p1] or p1<0:
                nums1[i] = nums2[p2]
                p2-=1
            else:
                nums1[i] = nums1[p1]
                p1-=1
            print(nums1)
            i-=1