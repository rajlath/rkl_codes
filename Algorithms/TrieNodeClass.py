class TrieNode(object):
    """
    an implementation of Trie
    """
    def __init__(self,char:str):
        self.char = char
        self.children = []
        self.word_done = False
        self.counter   = 1

def add(root, word: str):
    """
    adding a word to Trie
    """
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node = new_node
            print(node.children)
    node.word_done = True

def find_prefix(root, prefix:str):
    """"
    check and return
    1.does prefix exists in any of the words added so far
    2.If yes count how many words have that prefix
    """
    node = root
    """
    if node has no words return False
    """
    if not root.children:
            return (False, 0)
    for char in prefix:
        char_not_found = True
        """
        search all children of current node
        """
        for child in node.children:
            if child.char is char:
                char_not_found = False
            node = child
            break
    if char_not_found:return (False, 0)
    return (True, node.counter)

root = TrieNode("*")
add(root, "hackathon")
add(root, "hack")
print(root.children)
print(find_prefix(root, "hack"))




