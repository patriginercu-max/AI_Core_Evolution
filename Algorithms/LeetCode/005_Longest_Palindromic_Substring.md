*力扣第 5 题：最长回文子串（Longest Palindromic Substring）深度解构
**Ⅰ. 核心挑战点：回文特性的多维解析 (Challenge Points)奇偶形态差异：回文串有两种基本形态：奇数长度（如 aba，中心是一个字符）和偶数长度（如 abba，中心是两个字符间的空隙）。
算法必须同时覆盖这两种物理结构。时空复杂度权衡：
时间：暴力解法 $O(n^3)$ 会超时。必须通过动态规划或中心扩展法优化至 $O(n^2)$。
空间：动态规划需开辟 $N \times N$ 的 dp 表，空间成本高；中心扩展法可将空间复杂度降至最优的 $O(1)$。
索引换算的陷阱：在确定回文长度后，利用中心索引 $i$ 反推子串在原字符串中的起始位置（start）和结束位置（end）极易出现 $\pm 1$ 的错误。
**Ⅱ. 核心代码实现：中心扩展法的标准模版 (Code Implementation)这是面试中最推荐的解法，平衡了代码简洁度与空间效率。Pythonclass Solution:
    def longestPalindrome(self, s: str) -> str:
        # 【前置检查】长度小于2的字符串直接返回
        if not s or len(s) < 2:
            return s
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # 1. 尝试以 i 为中心进行奇数扩展 (如 "aba")
            len1 = self.expandAroundCenter(s, i, i)
            # 2. 尝试以 i 和 i+1 之间的间隙为中心进行偶数扩展 (如 "abba")
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # 取当前位置两种中心情况下的最长长度
            max_len = max(len1, len2)
            
            # 3. 更新全局最长记录的起始和结束索引
            if max_len > (end - start + 1):
                # 统一计算技巧：(max_len - 1) // 2 修正了偶数中心偏左的问题
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Python 切片左闭右开，故需要 end + 1
        return s[start : end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 向两端搜索，直到字符不相等或索引越界
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 【关键】退出循环时 s[left] != s[right]，跨度为 (right-1) - (left+1) + 1
        return right - left - 1
*Ⅲ. 核心逻辑拆解：数学推导与执行细节 (Key Logic)跨度计算原理：right - left - 1 的来源是因为 while 停止时，指针已经指向了有效回文区间的外部（左边界减过头了，右边界加过头了）。
双中心取最值：在每个索引 i 处，算法通过 max(len1, len2) 确保无论最长回文是奇是偶，都能被捕捉到。Python 切片特性：使用 s[start : end + 1]。切片的“右开”设计使得子串长度计算简化为 (end + 1) - start，这正是我们在 if 判断中使用的长度。
*Ⅳ. 复杂度与进阶建议：算法演进之路 (Optimization & Tips)方案时间复杂度空间复杂度适用场景暴力解法$O(n^3)$$O(1)$字符串极短动态规划$O(n^2)$$O(n^2)$需要分析子问题重叠时中心扩展$O(n^2)$$O(1)$面试及常规工程实践最优选Manacher$O(n)$$O(n)$针对超大规模字符串的极致性能调试建议：如果验证时发现只返回一个字符，检查 expandAroundCenter 的 while 退出条件和 max_len 的更新逻辑。
延伸思考：此题的动态规划解法可以转化为“求原字符串与其反转字符串的最长公共子串”，但要注意非连续性匹配的干扰。
