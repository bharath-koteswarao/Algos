package Java.Datastructures.Queues;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by BK on 23-08-2017.
 */
public class QueFrontToStackTop {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < 10; i++) {
            queue.add(i);
        }
        System.out.println(queue);
        while (!queue.isEmpty()) stack.push(queue.remove());
        while (!stack.isEmpty()) queue.add(stack.pop());
        while (!queue.isEmpty()) stack.push(queue.remove());
        System.out.println("Stack is " + stack);
    }
}