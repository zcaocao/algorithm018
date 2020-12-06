class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1

        front = {start}
        back = {end}
        bank = set(bank)
        dist = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'TAG', 'G': 'ATC'}

        while front:
            dist += 1
            new_front = set()
            for gene in front:
                for i, s in enumerate(gene): # 将每一个基因串作为枚举对象，并返回下标i及对应的字母s
                    for c in change_map[s]: 
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in back:
                            return dist
                        if new_gene in bank:
                            new_front.add(new_gene)
                            bank.remove(new_gene)
            front = new_front
            if len(back) < len(front):
                front, back = back, front
        return -1

        
