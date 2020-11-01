学习笔记

242 & 49 字母异位词系列
=======================
总体思路：一，排序分类； 二，按计数分类。

242.有效字母异位词
一，python可以直接sorted排序后判断两串是否相等，但时间复杂度较高，O(NlogN)。
二，根据字母计数哈希：
以字母作为key，字母出现次数作为value，其中，s串做➕操作，t串做➖操作。
最后，遍历哈希表的value（也就是字典），只要有value !=0，说明两串不完全相等。

49.字母异位词分组
同样根据上面两种思路。
一，先遍历每一个字符串，把字符串排序并查分成元组：
以每个有序元组作为key，value为字符串本身，遇到相同key的则append字符串。最后list返回字典的所有values对应的各自的字符串列表。
二，根据字母个数统计数组count为哈希key：
count初始化为26个0，遍历单词列表的每个单词，对单词的每个字母根据ascii码差值生成count列表（数组）。count相同的（key相同），append到对应value的列表里。


239 & 剑指 Offer 59 - I. 滑动窗口的最大值
==========================================
用双下标 i，j 标识窗口的左右边界，i 的范围是【1-k】，j 的范围是【0-n1】
注：未形成窗口前，i 有可能是负数的。

题目需要用deque来维护窗口有效值，所谓有效是指队头永远是当前窗口最大值，且deque单调减。

1.窗口左边界是通过判断deque头是否等于nums[i-1]，如果等于，说明队头已被移出窗口，所以队头也要删除，即deque.popleft()。
2.新元素nums[j]入窗口之前，先检查nums[j]是否大于deque内所有元素，如果大于，根据deque单调减的规则，pop掉deque内所有元素deque.pop()。
3.新元素nums[j]入队，deque.append(nums[j])
4.检查是否已形成端口(i>=0)，形成端口后，每入队一个元素则弹出一个当前窗口最大值（对头deque[0])到返回列表res。

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n - k + 1), range(n)):
            if i > 0 and deque[0] == nums[i - 1]: deque.popleft()
            while deque and deque[-1] < nums[j]: deque.pop()
            deque.append(nums[j])
            if i >= 0: res.append(deque[0])
        return res


 二叉树的遍历系列
=================
94.中序遍历
一，递归
二，迭代
思路：手动维护一个栈，进出栈原则，根先进栈，左子树不空就进栈，左子空就出栈，根出栈，根的右子不空就进栈，。。。。再重复上述进出栈。
计算机思维：
栈不空，或者根存在的情况下，就：
每次根进栈后，将其左子标记为新的根，然后只要根不空，循环遍历到整棵树的最左子进栈。
最左子进栈后，左子的左为空了，开始出栈，出栈节点append都返回列表里。同时，将出栈节点的右子设为新的根（再往复上面压栈的过程）。
Note：这里设置新的根时，没有判断当前根的左子或右子是否为空。因为，会在下一次循环时，走到相应的分支（为空就出栈，不空就继续进栈，右子为空时刚好保证根出栈）。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' iteration '''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                ans.append(tmp.val)
                root = tmp.right
        
        return ans        

三，莫里斯遍历
此方法优点是空间复杂度为O(1). 但改变了树的结构，将树毁成了链表。

144.二叉树的前序遍历

二，迭代思路类似中序，只是，返回序列值不是在出栈时拼接，而是在进站前先加入返回列表，当出栈时，只将右子设为root迭代进栈。


N叉树的遍历系列
================
589.前序
注意子节点入栈要“逆”序，以保证出栈时从左一开始，每出栈一个元素，入返回列表。
590.后序
后续注意没出栈一个元素，将其子节点“顺”序入栈，并将出栈元素入返回列表，最后结果是列表逆序输出。
429.层序

