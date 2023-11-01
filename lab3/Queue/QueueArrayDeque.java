package Queue;

import java.util.ArrayDeque;

public class QueueArrayDeque<T> implements Queue<T> {
    private ArrayDeque<T> queue = new ArrayDeque<>();

    @Override
    public void enqueue(T item) {
        queue.add(item);
    }

    @Override
    public T dequeue() {
        return queue.poll();
    }

    @Override
    public int size() {
        return queue.size();
    }

    @Override
    public boolean isEmpty() {
        return queue.isEmpty();
    }

    @Override
    public T front() {
        return queue.peekFirst();
    }

    @Override
    public T rear() {
        return queue.peekLast();
    }
}
