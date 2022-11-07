from collections import Counter, deque

class HaffmanTree:
    def __init__(self, s):
        self.s = s
        self.tree = None
        self.table_code = dict()

    @property
    def create_tree(self):
        count = Counter(self.s)
        sorted_elem = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_elem) != 1:
            while len(sorted_elem) > 1:
                weight = sorted_elem[0][1] + sorted_elem[1][1]
                comb = {0: sorted_elem.popleft()[0],
                        1: sorted_elem.popleft()[0]}
                for i, j in enumerate(sorted_elem):
                    if weight > j[1]:
                        continue
                    else:
                        sorted_elem.insert(i, (comb, weight))
                        break
                else:
                    sorted_elem.append((comb, weight))
        else:
            weight = sorted_elem[0][1]
            comb = {0: sorted_elem.popleft()[0], 1: None}
            sorted_elem.append((comb, weight))
        self.tree = sorted_elem[0][0]


    def create_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.table_code[tree] = path
            return self.table_code
        else:
            self.create_code(tree[0], path=f'{path}0')
            self.create_code(tree[1], path=f'{path}1')


s = "beep boop beer!"
haff = HaffmanTree(s)
haff.create_tree
haff.create_code(haff.tree)
for i in s:
    print(haff.table_code[i], end=' ')
