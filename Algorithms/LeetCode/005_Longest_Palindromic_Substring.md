# 力扣第 5 题：最长回文子串（Longest Palindromic Substring）深度解构

---

### Ⅰ. 核心挑战点 (Challenge Points)

1. 奇偶中心处理：回文中心既可以是字符（aba），也可以是字符间的空隙（abba）。
2. 复杂度优化：动态规划虽然逻辑清晰但空间复杂度达 O(n^2)，中心扩展法则优化至 O(1) 空间。
3. 索引反推陷阱：需要通过中心点 i 和算出长度 L 精确计算 start 和 end 的起始索引。

---

### Ⅱ. 核心代码实现 (Code Implementation)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 边界情况：长度小于 2 直接返回
        if not s or len(s) < 2:
            return s
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # 1. 奇数扩展（如 "aba"）
            len1 = self.expandAroundCenter(s, i, i)
            # 2. 偶数扩展（如 "abba"）
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # 取当前位置产生的最长回文长度
            max_len = max(len1, len2)
            
            # 3. 更新全局记录的起始和结束索引
            if max_len > (end - start + 1):
                # 核心公式：利用整除特性统一处理奇偶偏移
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Python 切片左闭右开，故为 end + 1
        return s[start : end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 向两边扩展，直到不满足回文条件
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 退出循环时，有效跨度为 right - left - 1
        return right - left - 1

---

### Ⅲ. 核心逻辑拆解 (Key Logic)

1. 长度公式推导：
   right - left - 1 是因为退出 while 循环时，left 和 right 都已经指向了回文区间外部。

2. 双中心机制：
   通过 expand(i, i) 和 expand(i, i + 1) 的并行计算，保证了算法不会漏掉偶数长度的情况。

3. 索引截取细节：
   使用 s[start : end + 1]。Python 中索引截取不包含尾部，必须 +1 才能取到索引为 end 的字符。



---

### Ⅳ. 复杂度与建议 (Optimization & Tips)

1. 复杂度分析：时间 O(n^2)，空间 O(1)。在力扣面试中这是综合表现最均衡的写法。
2. 验证与调试：若结果不对，建议 print(s[i:i+1]) 观察中心扩展的起点是否正确。
3. 进阶方向：针对超大规模字符串（n > 10^5），建议研究 Manacher 算法实现线性时间查找。
