学习笔记

### Trie树
```python
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

### 并查集
```python
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

OR

```python
f = {}

def find(x):
    f.setdefault(x, x)
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

def union(x, y):
    f[find(y)] = find(x)
```

### 高级搜索

##### 剪枝
##### 双向BFS

BFS模版
```python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

双向BFS(自己总结)
```python
def BFS(graph, start, end):
    front = {start}
    back = {end}
    dist = 0
    graph = set(graph)

	while front: 
        dist += 1
        new_front = set()
        for node in front:
		    visited.add(node)
		    new_node = process(node) 
            if new_node in back:
                return dist
		    new_front.add(new_node)
            update(graph)

        ront = new_front
        if len(back) < len(front):
            front, back = back, front
    
	# other processing work 
	...
```

##### 启发式搜索 Heuristic Search (A*)
```python
def AstarSearch(graph, start, end):

    pq = collections.priority_queue() # 优先级 —> 估价函数
    pq.append([start]) 
    visited.add(start)

    while pq:
        node = pq.pop() # can we add more intelligence here ? visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited] pq.push(unvisited)
```

###### 估价函数

启发式函数: 
h(n)，它用来评价哪些结点最有希望的是一个我们要找的结 点，h(n) 会返回一个非负实数,也可以认为是从结点n的目标结点路径的估 计成本。

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测 哪个邻居结点会导向一个目标。


### 高级树

#####  二叉搜索树 Binary Search Tree

二叉搜索树，也称二叉搜索树、有序二叉树(Ordered Binary Tree)、排序二叉树(Sorted Binary Tree)，是指一棵空树或者具有下列性质的二叉树:
1. 左子树上所有结点的值均小于它的根结点的值;
2. 右子树上所有结点的值均大于它的根结点的值;
3. 以此类推:左、右子树也分别为二叉查找树。 (这就是 重复性!)

中序遍历:升序排列


#####  AVL树

1. 发明者 G. M. Adelson-Velsky 和 Evgenii Landis
2. 平衡二叉搜索树
3. Balance Factor(平衡因子): 是它的左子树的高度减去它的右子树的高度(有时相反)。 balancefactor={-1, 0, 1}
4. 通过旋转操作来进行平衡(四种)

不足:结点需要存储额外信息、且调整次数频繁

##### 红黑树 Red-black Tree

红黑树是一种近似平衡的二叉搜索树(Binary Search Tree)，它能够确保任何一 个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉 搜索树:

• 每个结点要么是红色，要么是黑色
• 根结点是黑色
• 每个叶结点(NIL结点，空结点)是黑色的。
• 不能有相邻接的两个红色结点
• 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。
    
 ##### 对比
• AVL trees provide faster lookups than Red Black Trees because they are more strictly balanced.

• Red Black Trees provide faster insertion and removal operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.

• AVL trees store balance factors or heights with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.

• Red Black Trees are used in most of the language libraries
like map, multimap, multisetin C++whereas AVL trees are used in databases where faster retrievals are required.

