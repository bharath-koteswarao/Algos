package Datastructures.Stacks.Hackerrank_Problems;

import java.util.Scanner;
import java.util.Stack;

public class SimpleTextEditor {
    static Stack<String> operations = new Stack<>();
    static String answer = "";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        operations.push("");
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            int type = sc.nextInt();
            if (type == 1) {
                answer += sc.next();
                operations.push(answer);
            } else if (type == 2) {
                String toBeDeleted = answer.substring(answer.length() - sc.nextInt(), answer.length());
                answer = answer.replace(toBeDeleted, "");
                operations.push(answer);
            } else if (type == 3) {
                System.out.println(answer.charAt(sc.nextInt() - 1));
            } else {
                operations.pop();
                answer = operations.peek();
            }
        }
    }
}
