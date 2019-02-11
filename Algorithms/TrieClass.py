class Node(object):
    def __init__(self):
        self.children = {}
class Trie(object):
    def __init__(self)        :
        self.root = Node()
        self.root.data = "*"
def add_word_to_Trie(self, word):
    current_node = self.root
    i = 0
    for c in word:
        try
