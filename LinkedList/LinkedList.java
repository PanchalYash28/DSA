public class LinkedList {
    public static void main(String[] args) {
        MyLinkedList list = new MyLinkedList();
        list.add(10);
        list.add(20);
        list.add(30);
        list.add(40);
        list.add(50);
        list.add(60);
        list.add(70);
        list.add(80);
        list.add(90);
        // list.add(100);
        // list.add(110);
        // list.add(120);
        
        System.out.println("================================================");
        list.print();
        System.out.println("================================================");

        list.RemoveElementFromLast();
        list.print();
        System.out.println("================================================");

        list.RemoveFirstElement();
        list.print();
        System.out.println("================================================");

        System.out.println("Length of the LinkedList : "+list.FindLength());
        System.out.println("================================================");

        list.RemoveIndexedElement(1);
        list.print();
        System.out.println("================================================");

        System.out.println("Length of the LinkedList : "+list.FindLength());
        System.out.println("================================================");

        list.ReverseOfLinkedList();
        list.print();
        System.out.println("================================================");


    }
    
}

class MyLinkedList{
    Node head;

    void add(int YA){
        if (head == null) {
            head = new Node(YA);
            // System.out.println("Added: " + YA);
            return;
        }

        Node temp = head;

        while (temp.next != null) {
            temp = temp.next;            
        }
        temp.next = new Node(YA);
    }

///////////////////////////////////////////////////////////////////////////////////////

    void print(){
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        Node temp = head; // start at the head of the list // head copy................
        System.out.println("Head Data Elements of LinkedList : "+head.data);
        while (temp.next != null) {
            temp = temp.next;
            System.out.println("Data Elements of LinkedList : "+temp.data);
        }
    }

///////////////////////////////////////////////////////////////////////////////////////

    void RemoveElementFromLast(){
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        if (head.next == null) {
            head = null;
            return;
        }

        Node temp = head;

        while (temp.next.next != null) {
            temp = temp.next;
        }
        temp.next = null;
    }

///////////////////////////////////////////////////////////////////////////////////////

    void RemoveFirstElement(){
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        if (head.next == null) {
            head = null;
            return;
        }
        head = head.next;
    }

///////////////////////////////////////////////////////////////////////////////////////

    int FindLength(){
        int count = 0;
        Node temp = head;
        while (temp != null) { 
            count++;
            temp = temp.next;
        }
        return count;
    }

///////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////
    
    void RemoveIndexedElement(int index){
        if(head==null || index>=FindLength()){
        System.out.println("No element to remove");
        return;
        }

        Node temp = head;  // head copy

        for(int i=1;i<index;i++){
            temp = temp.next;
        }
        temp.next = temp.next.next;
    }

///////////////////////////////////////////////////////////////////////////////////////

    void ReverseOfLinkedList(){
        if(head==null || head.next==null){
            System.out.println("No element to revese");
            return;
        }
        Node prev = null;
        Node current = head;
        Node follow;
        while(current!=null){
            follow = current.next;
            current.next = prev;
            prev = current;
            current = follow;
        }
        head = prev;
    }

///////////////////////////////////////////////////////////////////////////////////////
    
}

class Node {
    int data;
    Node next;  // next node object

    Node(int data) {
        this.data = data;
        // this.next = next;
        next = null;
    }
}




==>>>output of above code:

Head Data Elements of LinkedList : 10
Data Elements of LinkedList : 20
Data Elements of LinkedList : 30
Data Elements of LinkedList : 40
Data Elements of LinkedList : 50
Data Elements of LinkedList : 60
Data Elements of LinkedList : 70
Data Elements of LinkedList : 80
Data Elements of LinkedList : 90
================================================
Head Data Elements of LinkedList : 10
Data Elements of LinkedList : 20
Data Elements of LinkedList : 30
Data Elements of LinkedList : 40
Data Elements of LinkedList : 50
Data Elements of LinkedList : 60
Data Elements of LinkedList : 70
Data Elements of LinkedList : 80
================================================
Head Data Elements of LinkedList : 20
Data Elements of LinkedList : 30
Data Elements of LinkedList : 40
Data Elements of LinkedList : 50
Data Elements of LinkedList : 60
Data Elements of LinkedList : 70
Data Elements of LinkedList : 80
================================================
Length of the LinkedList : 7
================================================
Head Data Elements of LinkedList : 20
Data Elements of LinkedList : 40
Data Elements of LinkedList : 50
Data Elements of LinkedList : 60
Data Elements of LinkedList : 70
Data Elements of LinkedList : 80
================================================     
Length of the LinkedList : 6
================================================     
Head Data Elements of LinkedList : 80
Data Elements of LinkedList : 70
Data Elements of LinkedList : 60
Data Elements of LinkedList : 50
Data Elements of LinkedList : 40
Data Elements of LinkedList : 20
================================================   
