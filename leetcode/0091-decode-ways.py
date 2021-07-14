mapping = {int(i): c for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}

def num_decodings(text):
    p1, p2 = 1, 0
    for i in range(len(text) - 1, -1, -1):
        print(text[i])

class Solution(object):
    def numDecodings(self, s):
        pass

num_decodings('test')
