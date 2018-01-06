class LinkedList {

    Node head;
    Node tail;

    /*
     * Adds Node to end of list with given `num` as data
     * Make sure it correctly sets the head (and tail) 
     * when adding the first item to the list
     */
    public void add(int num){
        // your code here
        if(head == null){ 
                 head = tail = new Node(num);
		 head.data = num;
		 head.next = tail;
		 tail = head;
		 }
   else{
		tail.next = new Node(num); //add a new node to the end of the list
		tail = tail.next; //set the tail pointer to that node
		tail.data = num; //set elem to be stored to the end node
		}	
        
    }

    /*
     * Returns value of node at given index
     */
    public int get(int index){
        // your code here
       Node temp = head; //start at the head of the list
  
     //iterate to the correct node
      for(int i = 0; i < index; i++) temp = temp.next; 
      return temp.data; //and return the corresponding element
    }
}

class Node{
    int data;
    Node next;
    public Node(int d){
      data = d;
    }

    public Node(int d, Node n){
        data = d;
        next = n;
    }
}

public class Main {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        for(int i=0; i<n; i++){
            int a = in.nextInt();
            int b= in.nextInt();
            if(a == -6){
                System.out.println(list.get(b)); 
            }
            else if(a == -9){
                list.add(b);
            }
        }
    }
}
