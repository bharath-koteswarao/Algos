package Java.Queues;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by BK on 13-08-2017.
 */
public class ReverseQ {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < 10; i++) q.add(i);
        System.out.println(q);
        while (!q.isEmpty()) stack.push(q.remove());
        while (!stack.isEmpty()) q.add(stack.pop());
        System.out.println(q);
    }
}
