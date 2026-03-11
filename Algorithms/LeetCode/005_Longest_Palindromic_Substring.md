# 力扣第 5 题：最长回文子串（Longest Palindromic Substring）深度解构

---

## Ⅰ. 核心挑战点 (Challenge Points)

* **奇偶中心处理**：回文中心既可以是字符，也可以是字符间的空隙。
* **复杂度优化**：动态规划虽然逻辑清晰但空间复杂度达 $O(n^2)$，中心扩展法则优化至 $O(1)$ 空间。
* **索引反推陷阱**：如何通过中心点 $i$ 和算出长度 $L$ 精确计算 `start` 和 `end` 的索引。

---

## Ⅱ. 核心代码实现 (Code Implementation)

```python
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

## Ⅲ. 核心逻辑拆解 (Key Logic)长度公式推导：

right - left - 1 是因为退出 while 循环时，left 和 right 都已经指向了回文区间外的一个位置。
**双中心机制：**通过 expand(i, i) 和 expand(i, i + 1) 的并行计算，保证了算法不会漏掉偶数长度的情况。
**索引截取细节：**s[start : end + 1]。Python 中索引截取不包含尾部，必须 +1 才能取到 end 指向的字符。
## Ⅳ. 复杂度与建议 (Optimization & Tips)

**复杂度：**时间 $O(n^2)$，空间 $O(1)$。面试中这是最优性价比的写法。
**打印验证：**如果验证不通过，建议在 if max_len 后打印 s[start:end+1] 观察截取过程。
**进阶方向：**面对数据规模 $n > 10^5$ 的极限场景，可进一步学习 Manacher 算法（线性时间）。
