function Node(data)
{
    this.data = data;
    this.left = null;
    this.right= null;
}

//create nodes
var root = new Node("A");
var   n1 = new Node("B");
var   n2 = new Node("C");
var   n3 = new Node("D");
var   n4 = new Node("E");

//set up children
root.left = n1;
root.right= n2;
n1.left   = n3;
n1.right  = n4;

function pre_order(root, nodes)
//get root.data, traverse root.left, root.right recursively
{
    nodes.push(root.data);
    if (root && root.left)
    {
        pre_order(root.left, nodes)
    }
    if (root && root.right)
    {
        pre_order(root.right, nodes)
    }

    return nodes;

}

pre_order(root, []);

function in_order(root, nodes)
//traverse left recursively, get root.data, traverse right recursively
{
    if (root && root.left)
    {
        in_order(root.left, nodes)
    }
    nodes.push(root.data)
    if(root && root.right)
    {
        in_order(root.right, nodes)
    }
    return nodes

}

in_order(root, []);

function post_order(root, nodes)
// root.left, root.right, root.data
{
    if (root && root.left)
    {
        post_order(root.left, nodes);
    }
    if (root && root.right)
    {
        post_order(root.right, nodes);
    }
    nodes.push(root.data);
    return nodes;
}

post_order(root, []);
//root in queue, pop last node , add all children of poped node to queue

function level_order(root, nodes)
{
    var queue = [root]
    while (queue.length > 0
        //front = element 0 , push element to back
        {
            var n = queue.shift();
            nodes.push(n.data);
            if(n.left != null){ queue.push(n.left) }
            if(n.right!= null){ queue.push(n.right)}
        }
    return nodes;
}
level_order(root, []);

