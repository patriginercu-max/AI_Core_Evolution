力扣第 5 题：最长回文子串（Longest Palindromic Substring）深度解构
Ⅰ. 核心挑战点：回文特性的多维解析 (Challenge Points)
奇偶形态差异：回文串有两种基本形态：奇数长度（如 aba，中心是一个字符）和偶数长度（如 abba，中心是两个字符间的空隙）。算法必须同时覆盖这两种物理结构。

时空复杂度权衡：

时间：暴力解法 O(n 
3
 ) 在 n=1000 时会超时。必须通过动态规划或中心扩展法优化至 O(n 
2
 )。

空间：动态规划需开辟 N×N 的 dp 表，空间成本高；中心扩展法可将空间复杂度降至最优的 O(1)。

索引换算的陷阱：在确定回文长度后，利用中心索引 i 反推子串在原字符串中的起始位置（start）和结束位置（end）极易出现 ±1 的计算错误。

Ⅱ. 核心代码实现：中心扩展法的标准模版 (Code Implementation)
这是面试中最推荐的解法，平衡了代码简洁度与空间效率。

Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 【前置检查】长度小于 2 的字符串，其本身就是最长回文
        if not s or len(s) < 2:
            return s
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # 1. 假设中心是奇数长度（如 "aba"，中心是 "b"）
            len1 = self.expandAroundCenter(s, i, i)
            # 2. 假设中心是偶数长度（如 "abba"，中心是 "bb" 之间的空隙）
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # 取当前位置两种中心情况下的最长长度
            max_len = max(len1, len2)
            
            # 3. 如果发现更长的回文串，更新记录的起始位置和结束位置
            if max_len > (end - start + 1):
                # 统一计算技巧：(max_len - 1) // 2 修正了偶数中心偏左的问题
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Python 切片左闭右开，故需要 end + 1 才能包含最后一个字符
        return s[start : end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 向两端搜索，直到字符不相等或索引越界
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 【关键】退出循环时 s[left] != s[right]
        # 有效区间是 [left + 1, right - 1]，长度为 (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
Ⅲ. 核心逻辑拆解：数学推导与执行细节 (Key Logic)
跨度计算原理：right - left - 1 的来源是因为 while 停止时，指针已经指向了有效回文区间的外部（左边界多减了 1，右边界多加了 1）。

双中心取最值：在每个索引 i 处，同时探测以字符为中心和以间隙为中心的情况，确保不漏掉任何偶数回文。

Python 切片特性：使用 s[start : end + 1]。Python 的切片是“左闭右开”的，为了包含索引为 end 的字符，终止位置必须是 end + 1。

Ⅳ. 复杂度与进阶建议：算法演进之路 (Optimization & Tips)
方案	时间复杂度	空间复杂度	适用场景
暴力解法	O(n 
3
 )	O(1)	仅限字符串极短时
动态规划	O(n 
2
 )	O(n 
2
 )	适合学习状态转移逻辑
中心扩展	O(n 
2
 )	O(1)	面试及常规工程实践最优选
Manacher	O(n)	O(n)	针对超大规模字符串的极致性能
调试建议：如果验证时发现只返回一个字符，优先检查 expandAroundCenter 的 while 退出条件和 max_len 的更新逻辑。

进阶方向：如果追求极致性能（如处理 10 万长度的字符串），可以研究 Manacher 算法，它通过“回文半径数组”规避了大量重复计算。
