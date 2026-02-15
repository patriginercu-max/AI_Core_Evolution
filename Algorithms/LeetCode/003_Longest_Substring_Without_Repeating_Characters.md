# LeetCode 003. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)

## 1. 题目深度分析
本题的核心是在给定字符串 $s$ 中寻找一个最长的子区间，要求该区间内不含任何重复字符。

* **核心算法**：**滑动窗口 (Sliding Window)**。通过维护一个窗口 $[left, right]$，动态调整其边界来捕获所有可能的无重复子串。
* **关键挑战**：当右指针 $right$ 遇到重复字符时，如何避免将窗口从头开始扫描（导致 $O(n^2)$），而是通过“精准跳跃”左指针 $left$ 来实现 $O(n)$ 的线性效率。
* **状态记录**：使用 **哈希表 (Dictionary)** 记录每个字符最后出现的索引位置，这是实现“精准跳跃”的基础。

---

## 2. 算法实现与代码细节
以下是基于 Python 的最优解法。代码中包含了关于指针移动和字典更新的详细注释。

```python
def lengthOfLongestSubstring(s: str) -> int:
    # 字典记录：字符 -> 其最近一次出现的下标索引
    char_map = {}
    left = 0
    max_length = 0
    
    # right 指针不断向右探索
    for right in range(len(s)):
        # 逻辑点：如果当前字符已存在且其上一次出现的位置在当前窗口 [left, right] 之内
        if s[right] in char_map and char_map[s[right]] >= left:
            # 左指针直接“跳跃”到重复字符上次出现位置的下一位
            # 这里的判断 char_map[s[right]] >= left 防止了 left 往回跳
            left = char_map[s[right]] + 1
        
        # 无论是否重复，都更新当前字符的最新的下标位置
        char_map[s[right]] = right
        
        # 计算当前有效窗口长度：(右边界 - 左边界 + 1)
        # 并使用 max 更新全局最高纪录，保留历史出现过的最长子串长度
        max_length = max(max_length, right - left + 1)
        
    return max_length```


3. 复杂度与性能评估维度复杂度说明时间复杂度$O(n)$字符串 $s$ 的长度为 $n$。尽管包含嵌套的字典操作，但由于哈希表查询为 $O(1)$，且双指针均保持单向向右移动，整体呈线性增长。空间复杂度$O(m)$$m$ 为字符集的大小（字符集上限）。字典 char_map 最多存储当前已知的所有不同字符及其最新索引。

4. 关键逻辑总结与避坑指南滑动窗口的“伸缩”机制：伸（Right）：通过 right 指针不断向右扩张，探测新的字符。缩（Left）：当发现重复且重复点在窗口内时，左指针 left 瞬间跳跃到重复点的下一位，而不是步进式移动。指针“不回跳”原则：代码中的 char_map[s[right]] >= left 是防止指针回跳的关键。场景示例：在处理 "abba" 时，遇到最后一个 'a'，其在字典记录的位置是索引 0。此时 left 已经在索引 2（处理第二个 'b' 时移动的）。如果没有这个判断，left 会跳回 1，导致逻辑崩溃。max() 函数的双重角色：在更新 left 时，max 保证窗口边界只进不退。在更新 max_length 时，它充当了全场比赛的“最高分纪录仪”，确保在窗口大小波动的过程中，始终保留历史上出现过的最大长度。
