import Queue.QueueArrayDeque;
import Queue.QueueLinkedList;
import Queue.QueueNode;
import Stack.StackArrayDeque;
import Stack.StackLinkedList;
import Stack.StackNode;

public class Main {

    public static void main(String[] args) {

        // Test Stack.StackArrayDeque
        System.out.println("StackArrayDeque");
        StackArrayDeque<String> stackArrayDeque = new StackArrayDeque();
        stackArrayDeque.push("a");
        stackArrayDeque.push("b");
        stackArrayDeque.push("c");
        System.out.println(stackArrayDeque.pop());  // Output: 'c'
        System.out.println(stackArrayDeque.size());  // Output: 2
        System.out.println(stackArrayDeque.peek());  // Output: 'b'
        System.out.println(stackArrayDeque.isEmpty());  // Output: false

        // Test Stack.StackLinkedList
        System.out.println("\nStackLinkedList");
        StackLinkedList<String> stackLinkedList = new StackLinkedList();
        stackLinkedList.push("a");
        stackLinkedList.push("b");
        stackLinkedList.push("c");
        System.out.println(stackLinkedList.pop());  // Output: 'c'
        System.out.println(stackLinkedList.size());  // Output: 2
        System.out.println(stackLinkedList.peek());  // Output: 'b'
        System.out.println(stackLinkedList.isEmpty());  // Output: false

        // Test Stack.StackNode
        System.out.println("\nStackNode");
        StackNode<String> stackNode = new StackNode();
        stackNode.push("a");
        stackNode.push("b");
        stackNode.push("c");
        System.out.println(stackNode.pop());  // Output: 'c'
        System.out.println(stackNode.size());  // Output: 2
        System.out.println(stackNode.peek());  // Output: 'b'
        System.out.println(stackNode.isEmpty());  // Output: false

        // Test Queue.QueueArrayDeque
        System.out.println("\nQueueArrayDeque");
        QueueArrayDeque<String> queueArrayDeque = new QueueArrayDeque();
        queueArrayDeque.enqueue("a");
        queueArrayDeque.enqueue("b");
        queueArrayDeque.enqueue("c");
        System.out.println(queueArrayDeque.dequeue());  // Output: 'a'
        System.out.println(queueArrayDeque.size());  // Output: 2
        System.out.println(queueArrayDeque.isEmpty());  // Output: false
        System.out.println(queueArrayDeque.front());  // Output: 'b'
        System.out.println(queueArrayDeque.rear());  // Output: 'c'

        // Test Queue.QueueLinkedList
        System.out.println("\nQueueLinkedList");
        QueueLinkedList<String> queueLinkedList = new QueueLinkedList();
        queueLinkedList.enqueue("a");
        queueLinkedList.enqueue("b");
        queueLinkedList.enqueue("c");
        System.out.println(queueLinkedList.dequeue());  // Output: 'a'
        System.out.println(queueLinkedList.size());  // Output: 2
        System.out.println(queueLinkedList.isEmpty());  // Output: false
        System.out.println(queueLinkedList.front());  // Output: 'b'
        System.out.println(queueLinkedList.rear());  // Output: 'c'

        // Test Queue.QueueNode
        System.out.println("\nQueueNode");
        QueueNode<String> queueNode = new QueueNode();
        queueNode.enqueue("a");
        queueNode.enqueue("b");
        queueNode.enqueue("c");
        System.out.println(queueNode.dequeue());  // Output: 'a'
        System.out.println(queueNode.size());  // Output: 2
        System.out.println(queueNode.isEmpty());  // Output: false
        System.out.println(queueNode.front());  // Output: 'b'
        System.out.println(queueNode.rear());  // Output: 'c'

    }
}
