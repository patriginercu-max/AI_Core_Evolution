LeetCode 04. 寻找两个正序数组的中位数1. 核心思想：二分查找划分点 (Partitioning)这道题的精髓不在于“合并”，而在于**“寻找分割线”**。目标：在两个数组中各切一刀，将它们分成左、右两部分。平衡条件：数量平衡：左半部分的总数等于右半部分（或多一个）。数值有序：左侧所有数的最大值 $\le$ 右侧所有数的最小值。为何高效：利用数组的有序性，我们只需在短数组上二分查找切割位置 $i$，长数组的切割位置 $j$ 会联动确定。复杂度仅为 $O(\log(\min(m, n)))$。2. 关键技术点二分指针 (low, high)我们在短数组的索引范围 [0, m] 内进行二分。如果 nums1[i-1] > nums2[j]，说明 nums1 左边出多了，high 左移。如果 nums2[j-1] > nums1[i]，说明 nums1 左边出少了，low 右移。边界处理 (inf)当切刀划在数组边缘时（如 $i=0$ 或 $i=m$），左边或右边会变为空。float('-inf')：处理左侧为空，确保 max 比较时由于它足够小而不被选中。float('inf')：处理右侧为空，确保 min 比较时由于它足够大而不被选中。这避免了繁琐的越界检查，使逻辑高度统一。3. 完整 Python 代码实现Pythonfrom typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，优化二分查找效率
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2  # nums1 的划分点
            j = half_len - i       # nums2 的划分点
            
            # 处理边界情况：使用正负无穷大避免索引越界
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # 核心判断：左侧最大值是否小于等于右侧最小值
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # 找到完美划分点
                if (m + n) % 2 == 1:
                    # 总数为奇数，左侧最大值即中位数
                    return float(max(maxLeft1, maxLeft2))
                else:
                    # 总数为偶数，取中间两个数的平均值
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            elif maxLeft1 > minRight2:
                # nums1 分出的左半部分太大，切刀需要左移
                high = i - 1
            else:
                # nums1 分出的左半部分太小，切刀需要右移
                low = i + 1
        
        return 0.0

# 示例用法:
# sol = Solution()
# print(sol.findMedianSortedArrays([1, 2], [3, 4])) # 输出 2.5
4. 复杂度分析时间复杂度：$O(\log(\min(m, n)))$。我们只对较短的数组进行二分查找。空间复杂度：$O(1)$。只使用了常数个变量存储指针和边界值。
