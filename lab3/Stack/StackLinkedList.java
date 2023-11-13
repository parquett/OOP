package Stack;

import java.util.LinkedList;

public class StackLinkedList<T> implements Stack<T> {
    private LinkedList<T> stack = new LinkedList<>();

    @Override
    public void push(T item) {
        stack.push(item);
    }

    @Override
    public T pop() {
        return stack.pop();
    }

    @Override
    public int size() {
        return stack.size();
    }

    @Override
    public T peek() {
        return stack.peek();
    }

    @Override
    public boolean isEmpty() {
        return stack.isEmpty();
    }
}
