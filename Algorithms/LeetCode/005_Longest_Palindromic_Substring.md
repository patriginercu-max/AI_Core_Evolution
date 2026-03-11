力扣第 5 题：最长回文子串（Longest Palindromic Substring）Ⅰ. 核心挑战点 (Challenge Points)中心不确定性：回文中心可能是字符（奇数）或字符间隙（偶数）。时空权衡：DP 耗费 $O(n^2)$ 空间，中心扩展法则只需 $O(1)$ 空间。索引计算：需要通过中心点和长度，精确反推回文串的起始 start 和结束 end 坐标。Ⅱ. 核心代码实现 (Code Implementation)Pythonclass Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        start, end = 0, 0
        for i in range(len(s)):
            # 情况 1：奇数长度扩展 (中心是 s[i])
            len1 = self.expandAroundCenter(s, i, i)
            # 情况 2：偶数长度扩展 (中心是 s[i] 和 s[i+1] 之间的空隙)
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            max_len = max(len1, len2)
            
            # 更新最长子串的起始和结束索引
            if max_len > (end - start + 1):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 退出循环时，有效区间是 [left + 1, right - 1]
        # 长度 = (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
Ⅲ. 核心逻辑拆解 (Key Logic)长度计算公式：right - left - 1 是因为循环退出时，左右指针各多走了一步无效位置。索引反推公式：start = i - (max_len - 1) // 2：利用 // 2 的向下取整特性，统一处理了奇偶两种中心情况下的起始位置偏移。切片范围：s[start : end + 1] 确保包含了 end 位置的字符。Ⅳ. 复杂度与建议 (Optimization & Tips)复杂度分析：时间复杂度 $O(n^2)$，空间复杂度 $O(1)$。调试技巧：如果发现输出为空，检查 while 循环中的 s[left] == s[right] 判断是否写错。进阶方案：如果 $n > 10^5$，建议学习 Manacher 算法实现 $O(n)$ 的线性查找。这段代码和总结应该可以在力扣笔记中完美显示了。如果还需要我针对其他题目做类似的总结，随时告诉我！
