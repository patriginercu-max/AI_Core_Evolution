LeetCode 002: Add Two Numbers 知识归档
1. 核心挑战方向总结
链表遍历与指针操作： 由于链表节点在内存中不连续，必须通过 curr = curr.next 这种“接力”方式移动指针。在 Python 中，变量直接持有对象的引用，操作起来非常像 C++ 的指针。

进位逻辑 (Carry Logic)： 这是本题数学逻辑的核心。你需要同时处理：

当前位的数值：(sum % 10)

传递给下一位的进位：(sum // 10) 注意：即使两个链表都走完了，如果最后还有一个进位（carry = 1），也必须创建一个新节点。

哑结点 (Dummy Node) 的艺术： 为了避免在循环中不断判断“头节点是否为空”，我们先创建一个虚拟的 dummy 节点。它是新链表的“锚点”，最终返回 dummy.next 即可。

2. Python 链表类定义 (对照 C++ Constructor)
在 Python 中，__init__ 承担了 C++ 构造函数的职责：

Python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val    # 相当于 C++ 的成员变量赋值
        self.next = next  # 默认为 None，相当于 C++ 的 nullptr
3. 完整代码实现 (包含详细注释)
这段代码结合了你熟悉的 C++ 指针思维与 Python 的简洁语法：

Python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 创建哑结点，用于固定结果链表的头部
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # 只要还有数没加完，或者还有进位，就继续
        while l1 or l2 or carry:
            # 提取值：如果链表已经到底，则视值为 0 (类似 C++ 的判空)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # 计算当前总和及新进位
            total = v1 + v2 + carry
            carry = total // 10  # 整除取进位
            out_val = total % 10 # 取模得当前位的值
            
            # 创建新节点并挂在结果链表后
            curr.next = ListNode(out_val)
            
            # 移动指针 (相当于 p = p->next)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # 返回哑结点之后的真实链表头
        return dummy.next
4. 关键点回顾
代码整洁度：使用 v1 = l1.val if l1 else 0 这种写法可以极大简化判空逻辑，避免写嵌套的 if-else。

空间换时间：我们创建了一个全新的链表来存储结果，时间复杂度为 O(max(N, M))，其中 N 和 M 分别是两个链表的长度。
