# 力扣第 11 题：盛最多水的容器 (Container With Most Water) 完整解析报告

## 1. 挑战点与核心思路 (Challenge & Idea)
* 挑战点：
  - 效率瓶颈：暴力法 O(n²) 在处理大规模数据时会超时。
  - 指针逻辑：如何确保移动指针的过程中不会错过最优解。
* 核心思路：
  - 使用【双指针法】。面积 S = 宽度(right - left) * 最小高度 min(height[left], height[right])。
  - 贪心策略：每一次都移动“较矮”的那根柱子。
  - 原理：移动长板时，宽度变小且高度上限仍受限于短板，面积必减小；只有移动短板，才有可能换取更高的板来弥补宽度损失。

---

## 2. 代码实现与详细注释 (Code & Comments)

class Solution(object):
    def maxArea(self, height):
        # 初始化结果变量
        ans = 0
        # 定义左右双指针，分别指向数组首尾
        left = 0
        right = len(height) - 1
        
        while left < right:
            # 计算当前围成的面积
            current_width = right - left
            current_min_height = min(height[left], height[right])
            area = current_width * current_min_height
            
            # 更新全局最大面积
            if area > ans:
                ans = area
            
            # 【关键修正点】：
            # 使用 if-else 结构，确保在 height[left] == height[right] 时
            # 也会移动其中一个指针（此处移动右指针），彻底杜绝死循环。
            if height[left] < height[right]:
                left += 1
            else:
                # 处理了 height[right] < height[left] 以及相等的情况
                right -= 1
                
        return ans

---

## 3. 复杂度分析 (Complexity Analysis)
* 时间复杂度：O(n)。指针 left 和 right 仅向中心靠拢，总计遍历数组一次。
* 空间复杂度：O(1)。仅使用了 ans, left, right 等常数个额外变量，空间占用固定。

---

## 4. 常见误区与避坑指南 (Common Pitfalls)
* 死循环陷阱：你之前的代码用了两个独立的 if (if < 和 if >)。当遇到两根柱子等高时（如 [1, 1]），两个条件都不满足，指针会卡死在原地不动。
* 逻辑证明：记住“木桶效应”，容器能盛多少水取决于最短的那块板。因此，为了追求更大面积，必须尝试更换掉当前的短板。
* 运行环境：在 LeetCode 提交时，确保类名和方法名与题目要求完全一致。
