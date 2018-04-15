class Trie_Node(object):
    '''
    implements a Trie Node
    '''
    def __init__(self):
        self.children = [None] * 26
        self.is_end   = False

class Trie(object):
    '''
    implements a Trie data structure
    '''
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        '''
        return a Trie_Node initialized to Null
        '''
        return Trie_Node()

    def _char_to_index(self, ch):
        '''
        return index of ch in alphabet
        '''
        if ch.isupper():
            return ord(ch) - ord("A")
        else:
            return ord(ch) - ord("a")

    def insert(self, word):
        curr = self.root
        for ch in word:
            indx = self._char_to_index(ch)
            if not curr.children[indx]:
                curr.children[indx] = self.get_node()
            curr = curr.children[indx]
        curr.is_end = True


    def search(self, word):
        curr = self.root
        for ch in word:
            indx = self._char_to_index(ch)
            if not curr.children[indx]:
                return False
            curr = curr.children[indx]
        return curr != None and curr.is_end

test = Trie()
dicts= ["the","a","there","anaswe","any","by","their"]
output = ["Not present in trie", "Present in trie"]

for d in dicts:
    test.insert(d)

print("{} ----- {}".format("any", output[test.search("any")]))
print("{} ----- {}".format("he",  output[test.search("the")]))
print("{} ----- {}".format("raj", output[test.search("raj")]))











