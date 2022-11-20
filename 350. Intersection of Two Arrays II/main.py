class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        
        if nums1 > nums2:
            nums1, nums2 = nums2, nums1
        
        for i in nums2:
            d[i] = d.get(i, 0) + 1
        
        for i in nums1:
            if i in d and d.get(i, 0) > 0:
                res.append(i)
                d[i] = d.get(i, 0) - 1
        
        return res