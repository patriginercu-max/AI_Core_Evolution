# LeetCode 003. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)

---

## 1. 题目深度分析
本题核心是在 $O(n)$ 时间内寻找不含重复字符的最长连续子串。
* **核心算法**：滑动窗口 (Sliding Window)。
* **状态记录**：使用哈希表 (Dictionary) 记录字符及其出现的最新索引。
* **关键点**：利用索引实现左指针的“精准跳跃”。

---

## 2. 算法实现与逻辑 (Python)
(注：Github 粘贴后可手动在前后添加三个反引号以开启高亮)

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}  # 记录字符与其最新下标
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # 逻辑点：发现重复且重复点在当前窗口内
        if s[right] in char_map and char_map[s[right]] >= left:
            # 左指针跳跃到重复字符上次位置的下一位
            left = char_map[s[right]] + 1
            
        # 更新字符位置并计算最大长度记录
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length

---

## 3. 复杂度与性能评估

| 维度 | 复杂度 | 说明 |
| :--- | :--- | :--- |
| **时间复杂度** | $O(n)$ | 字符串长度为 $n$。双指针均保持单向移动，哈希表操作为 $O(1)$。 |
| **空间复杂度** | $O(m)$ | $m$ 为字符集的大小，字典最多存储所有不同字符的映射。 |

---

## 4. 关键逻辑总结与避坑指南

* **指针不回跳原则**：`char_map[s[right]] >= left` 是核心约束。例如处理 "abba" 时，处理到最后的 'a'，若无此判断，left 会从索引 2 跳回 1，导致窗口再次包含重复的 'b'。
* **滑动窗口本质**：右指针 (Right) 负责探索，左指针 (Left) 负责在违规时实现精准修正。
* **max() 的作用**：在更新 `max_length` 时，它充当了全场纪录仪，确保始终保留历史扫描过程中的峰值长度。
