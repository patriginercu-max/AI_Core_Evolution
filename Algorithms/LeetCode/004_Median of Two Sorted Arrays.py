# LeetCode 04. 寻找两个正序数组的中位数

---

## 1. 核心算法思想：二分查找划分点 (Partitioning)

这道题的精髓不在于“合并”，而在于**“寻找分割线”**。

* **逻辑目标**：在两个数组中各切一刀，将它们分成左、右两部分。
* **平衡条件**：
    1.  **数量平衡**：左半部分的总数等于右半部分（或多一个）。
    2.  **数值有序**：左侧所有数的最大值 $\le$ 右侧所有数的最小值。
* **为何高效**：利用数组的有序性，我们只需在**短数组**上二分查找切割位置 $i$，长数组的切割位置 $j$ 会联动确定。复杂度仅为 $O(\log(\min(m, n)))$。



---

## 2. 关键逻辑总结

### ① 二分指针 (low, high)
我们使用 `low` 和 `high` 来控制短数组 `nums1` 的切割点：
* 如果 `nums1[i-1] > nums2[j]`：说明 `nums1` 左边贡献多了，`high = i - 1`（左移）。
* 如果 `nums2[j-1] > nums1[i]`：说明 `nums1` 左边贡献少了，`low = i + 1`（右移）。

### ② 实例演示
以 `nums = [1, 3, 5, 7, 9]` 寻找 `7` 为例：二分查找每次对比中间值，如果不匹配，直接舍弃一半的搜索区间，实现对数级增长的速度。



### ③ 边界处理 (inf) 的妙用
当切刀划在数组边缘时（如 $i=0$ 或 $i=m$），左边或右边会变为空。
* **`float('-inf')`**：处理左侧为空，确保在取最大值时不会被选中。
* **`float('inf')`**：处理右侧为空，确保在取最小值时不会被选中。
**意义**：这套逻辑消灭了繁琐的越界检查，让代码极其优雅。

---

## 3. Python 代码实现

```python
from typing import List

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
            # 这种“一行式 if”写法让代码更简洁
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # 核心判断：左侧最大值是否小于等于右侧最小值
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # 找到完美划分点
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            elif maxLeft1 > minRight2:
                high = i - 1
            else:
                low = i + 1
        
        return 0.0
