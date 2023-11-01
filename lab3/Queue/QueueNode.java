package Queue;

public class QueueNode<T> implements Queue<T> {
    private Node<T> front, rear;

    public class Node<T> {
        T data;
        Node<T> next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    @Override
    public void enqueue(T data) {
        Node<T> node = new Node<>(data);

        if (rear == null) {
            front = rear = node;
            return;
        }

        rear.next = node;
        rear = node;
    }

    @Override
    public T dequeue() {
        if (front == null) return null;

        T data = front.data;

        front = front.next;

        if (front == null) rear = null;

        return data;
    }

    @Override
    public int size() {
        int count = 0;
        Node<T> current = front;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    @Override
    public boolean isEmpty() {
        return front==null;
    }
    @Override
    public T front() {
        return front.data;
    }

    @Override
    public T rear() {
        return rear.data;
    }
}
