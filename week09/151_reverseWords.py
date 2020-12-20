class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        return " ".join(reversed(s.split()))
        '''
        left, right = 0, len(s)-1
        # 去串头空格
        while left <= right and s[left] == ' ':
            left += 1
        # 去串尾空格
        while left <= right and s[right] == ' ':
            right -= 1
        
        q, word = collections.deque(), []
        while left <= right:
            # 遇到空格，且有组装完成的单词，就从队列头入队列
            if s[left] == ' ' and word:
                q.appendleft(''.join(word))
                word = []
            # 只要不是空格，就组装成单词
            elif s[left] != ' ':
                word.append(s[left])
            # 遇到词间有多个空格时，直接跳过，不做任何处理
            left += 1
        # 最后一个单词由于结尾没有空格，因此不会落入第一个if分支，所以单独append一次
        q.appendleft(''.join(word))
        
        return ' '.join(q)
