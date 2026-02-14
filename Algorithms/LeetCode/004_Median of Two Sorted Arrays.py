
def findMedianSortedArrays(nums1, nums2):
    # 确保 nums1 是较短的数组，优化二分查找效率
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        i = (low + high) // 2  # nums1 的划分点
        j = (m + n + 1) // 2 - i  # nums2 的划分点
        
        # 边界处理：如果划分点在数组最左侧，设为负无穷；在最右侧，设为正无穷
        maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
        minRight1 = float('inf') if i == m else nums1[i]
        
        maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
        minRight2 = float('inf') if j == n else nums2[j]
        
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # 找到完美的划分点
            if (m + n) % 2 == 0:
                # 偶数情况：取左侧最大和右侧最小的平均值
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            else:
                # 奇数情况：左侧最大值即为中位数
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            # nums1 左边太大，需要向左收缩
            high = i - 1
        else:
            # nums1 左边太小，需要向右扩展
            low = i + 1
