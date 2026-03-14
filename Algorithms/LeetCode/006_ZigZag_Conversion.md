# 力扣第 6 题：Z 字形变换 (ZigZag Conversion) 深度解构

---

### Ⅰ. 核心挑战点 (Challenge Points)

1. 转向逻辑：如何通过单一变量控制行索引在 [0, numRows-1] 之间循环“折返”（从 0 增加到底，再从底减回到 0）。
2. 边界陷阱：当 numRows = 1 时，`curRow == 0` 和 `curRow == numRows - 1` 同时成立，会导致方向判断失效，必须特判直接返回。
3. 字符串拼接效率：在 Python 中频繁对字符串使用 `+` 拼接会产生大量临时对象，影响性能。

---

### Ⅱ. 核心代码实现 (Code Implementation)

class Solution:
    def convert(self, s, numRows):
        # 边界处理：行数小于 2 或大于字符串长度，结果就是原串
        if numRows < 2 or numRows >= len(s):
            return s
        
        # 1. 创建 numRows 个桶，每个桶代表一行
        rows = [""] * numRows
        curRow = 0
        goingDown = False 
        
        # 2. 遍历字符串，模拟折返路径
        for c in s:
            rows[curRow] += c
            # 触顶或触底时翻转方向
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            
            # 根据方向决定下一行
            curRow += 1 if goingDown else -1
            
        # 3. 将所有行拼接成最终结果
        # "".join(rows) 意思是将列表里的每一行字符串按顺序连接起来
        return "".join(rows)

---

### Ⅲ. 核心逻辑拆解 (Key Logic)

1. "".join(rows) 的深层含义：
   - 假设 rows = ["P", "A", "Y"]，执行结果就是 "PAY"。
   - 引号里的内容是“连接符”。如果是 "-".join(["A", "B"])，结果就是 "A-B"。
   - 效率：Python 字符串是不可变的。使用 `join` 会预先计算总长度并一次性分配内存，比在循环里不断用 `+` 拼接快得多。

2. 桶排序思想：
   我们不需要关心字符在 Z 字形中具体的列坐标，只需要关心它属于哪一行。最后按行顺序读取即可。

3. goingDown 初始设为 False 的巧妙：
   当遍历第 1 个字符时（curRow=0），`if` 触发翻转，`goingDown` 瞬间变为 True，随后执行 `curRow += 1` 移向下一行。



---

### Ⅳ. 复杂度与建议 (Optimization & Tips)

1. 复杂度分析：时间 O(n)，空间 O(n)。我们需要遍历一遍字符串，并存储所有字符。
2. 性能建议：永远优先使用 `"".join(list)` 而不是循环内的 `res += s`。
3. 面试陷阱：如果 numRows = 1，由于 `curRow == 0` 和 `curRow == numRows - 1` 始终相等，方向会不停地 False/True 切换，导致死循环或逻辑混乱。
