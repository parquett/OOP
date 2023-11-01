package Stack;

public class StackNode<T> implements Stack<T> {
    private Node<T> top;
    private int size = 0;

    private class Node<T> {
        T data;
        Node<T> next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    @Override
    public void push(T data) {
        Node<T> node = new Node<>(data);
        node.next = top;
        top = node;
        size++;
    }

    @Override
    public T pop() {
        if (top == null) return null;

        T data = top.data;
        top = top.next;
        size--;

        return data;
    }

    @Override
    public T peek() {
        if (top == null) return null;

        return top.data;
    }

    @Override
    public boolean isEmpty() {
        return top == null;
    }

    @Override
    public int size() {
        return size;
    }
}
