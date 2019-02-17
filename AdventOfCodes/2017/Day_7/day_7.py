from collections import namedtuple, defaultdict
import re

def get_lines():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line)
    return lines


def build_tree():
    programs = []
    lines = get_lines()
    regex = re.compile('(.+) \((\d+)\)( -> )?(.+)?')
    for  line in lines:
        data = regex.match(line)
        node = data.group(1)
        weight=int(data.group(2))
        children = ()
        if type(data.group(4)) == str:
            children = data.group(4).split(", ")
        programs.append((node, weight, children))
    return programs

def do_part_1():
    tree = build_tree()
    leaves=set()
    nodes =set()
    x = 5
    for i in tree:
        node, weight, children = i
        x -= 1
        print(node,weight, children)
        nodes.add(node)
        if len(children) > 0:
            for j in children:
                leaves.add(j)
                nodes.add(j)
    #print(nodes, leaves)
    root = list(nodes - leaves)
    return root

def do_part_2(root):
    tree = build_tree()
    nodes  = {}
    weights= {}
    for p in tree:
        node, weight, children = p

    def solve(root):
        node, weight, children = nodes[root]
        if children:
            for c in children:
                weight = solve(c)
                if weight:
                    return weight
            cost = min(weights[c] for c in children)
            for c in children:
                if weights[c] != cost:
                    c_node, c_weight, c_children = node[c]
                    weight = cost - sum(weight[c] for c in c_children)
                    return weight
            weights[node] = weight + len(children) * cost
        else:
            weights[node] = weight

    return solve(root)


do_part_1()
source = do_part_1()
weight = do_part_2(source)
print(weight)



