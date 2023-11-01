package Queue;

public interface Queue<T> {
    void enqueue(T item);
    T dequeue();
    int size();
    boolean isEmpty();
    T front();
    T rear();
}
