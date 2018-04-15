Class Node{
  public:
  node *left, *right, *parent;
  int leftc;
  int key;
  int val;
  node(int _key=0):key(_key){
  left=NULL; right = NULL; parent=NULL;
val=0; leftc=0;}
}

by calling the following function from the last element to the first one, you can get the result in ave O(nlogn), worst O(n^2);

int revised_insert(node*& root, node* new){
node* curr=root;
node*tmp=NULL;
while(curr!=NULL){
tmp=curr;
if(new->key>curr->key){
curr->leftc++;
curr=curr->left;}
else{
new->value+=curr->leftc+1;
curr=curr->right;}
}
//update links
new->parent=tmp;
if (tmp==NULL)
root=new;
else if(new->key<tmp->key)
tmp->left=new;
else tmp->right=new;
//return result
return new->value;
}