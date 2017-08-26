package Datastructures.Queues;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

/**
 * Created by BK on 13-08-2017.
 */
public class Reverse_K_Elements {
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < 10; i++) {
            q.add(i);
        }
        System.out.println(q);
        Stack<Integer> stack = new Stack<>();
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of elements to reverse : ");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            stack.add(q.remove());
        }
        while (!stack.isEmpty()) q.add(stack.pop());
        System.out.println(q);
        for (int i = 0; i < q.size() - n; i++) {
            q.add(q.remove());
        }
        System.out.println(q);
    }
}
