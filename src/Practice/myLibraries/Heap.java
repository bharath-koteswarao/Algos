package myLibraries;

import java.util.Collection;
import java.util.PriorityQueue;

/**
 * Created by bk on 16-06-2018.
 */
public class Heap<E> {

    private PriorityQueue<E> queue;
    private E temp;
    private boolean added = false;

    public Heap(Collection<E> collection, E temp) {
        queue = new PriorityQueue<>(collection);
        this.temp = temp;
    }

    public Heap(E temp) {
        queue = new PriorityQueue<>();
        this.temp = temp;
    }

    public E pop() {
        return queue.poll();
    }

    public E peek() {
        return queue.peek();
    }

    public void add(E e) {
        queue.add(e);
        heapify();
    }


    public void remove(E e) {
        queue.remove(e);
        heapify();
    }

    public void heapify() {
        if (added) queue.remove(temp);
        if (!added) queue.add(temp);
        added = !added;
    }

    @Override
    public String toString() {
        return this.queue + "";
    }
}
