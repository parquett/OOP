package Queue;

import java.util.LinkedList;

public class QueueLinkedList<T> implements Queue<T>{
    private LinkedList<T> queue = new LinkedList<>();

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
