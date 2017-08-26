package Datastructures.Stacks.Hackerrank_Problems;

import java.util.Scanner;
import java.util.Stack;

/**
 * Created by BK on 06-08-2017.
 */
public class MaximumElement {
    public static void main(String... strings) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> maxStack = new Stack<>();
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            int flag = sc.nextInt();
            if (flag == 1) {
                int num = sc.nextInt();
                stack.push(num);
                if (maxStack.isEmpty()) maxStack.push(num);
                else {
                    if (maxStack.peek() <= num) maxStack.push(num);
                    else {
                        maxStack.push(maxStack.peek());
                    }
                }
            } else if (flag == 2) {
                stack.pop();
                maxStack.pop();
            } else {
                System.out.println(maxStack.peek());
            }
        }
    }
}
