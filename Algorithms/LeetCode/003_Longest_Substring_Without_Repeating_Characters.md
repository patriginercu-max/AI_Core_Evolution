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
        
    return max_length
3. 复杂度评估该算法通过单次遍历（双指针单向移动）实现了极高的性能。维度复杂度说明时间复杂度$O(n)$字符串 $s$ 仅被完整遍历一次，字典操作的时间复杂度为 $O(1)$。空间复杂度$O(m)$$m$ 为字符集的大小（例如 ASCII 字符集为 128 或 256），字典存储这些映射。4. 总结与注意事项防止指针回跳：在更新 left 时，必须确保 char_map[s[right]] >= left。这是为了处理如 "abba" 这样的字符串，当遇到最后的 'a' 时，防止 left 跳回索引 1。max 函数的本质：max(max_length, ...) 充当了“全场纪录仪”，它并不参与状态转移的递推，只是为了在窗口大小波动时，捕捉并保留曾经出现过的最大值。适用场景：只要题目要求寻找连续子区间且涉及去重/计数，滑动窗口 + 哈希表通常是最优解模版。
