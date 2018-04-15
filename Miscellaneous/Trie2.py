from collections import defaultdict
class Trie(object):
    '''
    implements Trie data structrue
    methods include Insert Search Prefix
    '''
    def __init__(self):
        self.root = defaultdict()

    def insert(self, word):
        '''
        @param {String} word
        @return void
        inserts a word into the trie
        '''
        current = self.root
        for ch in word:
            current = current.setdefault(ch, {})
        current.setdefault("_end")

    def search(self, word):
        '''
        @param {string} word
        @return {boolean}
        searches trie for the word, return True if found else False
        '''
        current = self.root
        for ch in word:
            if ch not in current:
                return False
            current = current[ch]
        if "_end" in current:
            return True
        return False

    def start_with(self, prefix):
        '''
        @param {String} prefix
        @return {Boolean}
        searches for prefix in Trie, return True if found else False
        '''
        current = self.root
        for ch in prefix:
            if ch not in current:
                return False
            else:
                current = current[ch]
        return True



test = Trie()
test.insert("Raj")
test.insert("lath")
test.insert("Padma")
print(test.search("Lath"))
print(test.search("lath"))
print(test.start_with("la"))


