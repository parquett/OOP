package Stack;

import java.util.ArrayDeque;

public class StackArrayDeque<T> implements Stack<T> {
    private ArrayDeque<T> stack = new ArrayDeque<>();

    @Override
    public void push(T item) {
        stack.push(item);
    }

    @Override
    public T pop() {
        return stack.pop();
    }

    @Override
    public T peek() {
        return stack.peek();
    }

    @Override
    public int size() {
        return stack.size();
    }

    @Override
    public boolean isEmpty() {
        return stack.isEmpty();
    }
}
