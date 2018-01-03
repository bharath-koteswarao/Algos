from bisect import bisect_left as bs


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ma = nums1 if len(nums1) > len(nums2) else nums2
        mi = nums1 if len(nums1) < len(nums2) else nums2
        lma, lmi = len(ma), len(mi)
        start, end, ind = 0, lmi - 1, 0
        found = False
        while True:
            mid = (start + end) // 2
            ind = bs(ma, mi[mid])
            if lma % 2 == 0:
                if ind == lma // 2:
                    break
                elif ind < lma // 2:
                    start = mid + 1
                else:
                    end = mid
            else:
                if ind == lma // 2 or ind == (lma // 2) + 2:
                    break
            if start == end:
                found = True
                break
        if found:
            return float(mi[start])
        else:
            return float(mi[ind])


Solution().findMedianSortedArrays([1,3], [2])
