
def common_ancestor(n1, n2, head):
    """Return the nearest common ancestor of nodes n1 and n2 in the tree
    rooted at head.

    """
    count = 0   # How many nodes in {n1, n2} have been visited so far?
    ancestor = None

    def traverse(node):
        nonlocal count, ancestor
        if node is None or ancestor is not None: return
        count_at_entry = count
        if node is n1: count += 1
        if node is n2: count += 1
        traverse(node.left)
        traverse(node.right)
        if count_at_entry == 0 and count == 2 and ancestor is None:
            ancestor = node

    traverse(head)
    return ancestor
        
