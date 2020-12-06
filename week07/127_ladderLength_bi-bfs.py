''' bidirectional BFS '''
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        # 建立两个拓展集合：front和back
        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)

        while front: # 等同于 while front and back: 因为下面会取成员较少的集合优先遍历
            dist += 1
            next_front = set() # 用以保证每次遍历的是新加入的单词
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            # 头尾交汇，退出遍历返回当前路经数
                            if new_word in back:
                                return dist
                            # 新生成但是是给定单词列表中的成员，则加入当前遍历的集合，
                            # 同时未免被重复遍历到，应从给定单词集合（列表）中删除。
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)

            front = next_front
            # 每次优先取较小的集合遍历
            if len(back) < len(front):
                back, front = front, back

        return 0
        
