#impolementation of BST in python
#includes a method to create a BST from array
import random_array

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    def __str__(self):
        return 'value: {0}, count: {1}'.format(self.value, self.count)

def insert(root, value):
    if not root:
        return Node(value)
    elif root.value == value:
        root.count += 1
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def create(seq):
    root = None
    for word in seq:
        root = insert(root, word)
    return root

def search(root, word, depth=1):
    if not root:
        return 0, 0
    elif root.value == word:
        return depth, root.count
    elif word < root.value:
        return search(root.left, word, depth + 1)
    else:
        return search(root.right, word, depth + 1)

def print_tree(root):
    if root:
        print_tree(root.left)
        print (root)
        print_tree(root.right)




'''

src = ['foo', 'bar', 'foobar', 'bar', 'barfoo']
tree = create(src)
print_tree(tree)

for word in src:
    print ('search {0}, result: {1}'.format(word, search(tree, word)))

def main():
    words = ["raj", "rahul", "ritika", "padma", "vidha"]
    b = Binary_tree()
    b.insert(words)
    b.create_tree(b.root,words)
    b.print_tree()

main()
'''








