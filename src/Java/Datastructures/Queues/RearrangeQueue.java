package Java.Datastructures.Queues;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by BK on 23-08-2017.
 */
public class RearrangeQueue {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < 10; i++) {
            queue.add(i);
        }
        Stack<Integer> stack = new Stack<>();
        int n = queue.size() / 2;
        for (int i = 0; i < n; i++) {
            stack.push(queue.remove());
        }
        System.out.println(stack + " " + queue);
        for (int i = 0; i < n * 2; i++) {
            System.out.println(i % 2 == 0 ? queue.remove() : stack.pop());
        }
        System.out.println(queue);
    }
}
