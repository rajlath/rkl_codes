class Tree_Traversal
{
    public static void main(String[] args)
    {


    }
    public void inOrder(Node root){
        inOrder(root.left);
        System.out.println(root.data + " ");
        inOrder(root.right);
    }
    public void preOrder(Node root){
        System.out.println(root.data + " ");
        preOrder(root.left);
        preOrder(root.right);
    }
    public void postOrder(Node root){
        postOrder(root.left);
        postOrder(root.right);
        System.out.println(root.data + " ");
        }
}