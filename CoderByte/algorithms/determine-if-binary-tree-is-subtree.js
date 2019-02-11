function Node(data)
{
    this.data = data;
    this.left = null;
    this.right= null;
}

//sub tree
var root = new Node(10);
var n1   = new Node(4);
var n2   = new Node(6);
var n3   = new Node(30);

n1.right = n3;
root.left = n1;
root.right= n2;

// main tree

var root_r = new Node(26);
var n1_r   = new Node(10);
var n2_r   = new Node(3);
var n3_r   = new Node(4);
var n4_r   = new Node(6);
var n5_r   = new Node(3);
var n6_r   = new Node(30);

n3_r.right = n6_r;
n3_r.left  = n3_r;
n1_r.right = n4_r;
n2_r.left  = n5_r;
root_r.left = n1_r;
root_r.right= n2_r;

//algorithm is both the tree are traversed in_order and pre_order
//if in_order of sub tree is in main tree it is a sub tree
//if pre_order of one tree is in another tree it has a tree as sub tree in another tree

function in_order(root, nodes)
{
    if(root && root.left){ in_order(root.left, nodes); }
    nodes.push(root.data);
    if(root && root.right) { in_order(root.right, nodes); }
    return nodes;
}

function pre_order(root, nodes)
{
    nodes.push(root.data);
    if(root && root.left) { pre_order(root.left, nodes); }
    if(root && root.right){ pre_order(root.right, nodes);}
    return nodes;
}

//we take in two tree
//generate in_order and pre_order seq of both the tree
//if one seq is in another seq; there is a sub tree in another tree
function is_subtree(root, root_r)
{
    var inord1 = in_order(root, []).join("-");
    var inord2 = in_order(root_r, []).join("-");

    var preord1 = pre_order(root, []).join("-");
    var preord2 = pre_order(root_r, []).join("-");

    return inord2.indexOf(inord1) != -1 && preord2.indexOf(preord1) != -1;
}

log(is_subtree(root, root_r));



