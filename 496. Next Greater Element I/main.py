def main(nums1, nums2):
    out = []
    for i in nums1:
        index = nums2.index(i)
        for j in range(index, len(nums2)):
            if nums2[j] > i:
                out.append(nums2[j])
                index = -1
                break
        if index != -1:
            out.append(-1)
    return out


nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(main(nums1, nums2))