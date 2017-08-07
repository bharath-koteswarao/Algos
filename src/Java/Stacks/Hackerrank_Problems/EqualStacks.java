package Java.Stacks.Hackerrank_Problems;

import java.util.Scanner;
import java.util.Stack;

/**
 * Created by BK on 06-08-2017.
 */

/*
*       Solution not yet accepted
*
* */
public class EqualStacks {
    public static void main(String... strings) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        int max = Math.max(n1, Math.max(n2, n3));

        // Using this temp array I'm populating stacks

        int[] temp = new int[max];

        // Three stacks to hold three sets of cylinders

        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();
        Stack<Integer> s3 = new Stack<>();

        // Each of the below 3 blocks work in similar manner
        // They add the sum to stack
        // For example if input is 4, 3, 2 I'm adding this to stack
        // 2, (2+3), (2+3+4)
        for (int i = 0; i < n1; i++) {
            temp[i] = sc.nextInt();
        }
        int sum = 0;
        for (int i = n1 - 1; i >= 0; i--) {
            sum += temp[i];
            s1.push(sum);
        }


        for (int i = 0; i < n2; i++) {
            temp[i] = sc.nextInt();
        }
        sum = 0;
        for (int i = n2 - 1; i >= 0; i--) {
            sum += temp[i];
            s2.push(sum);
        }


        for (int i = 0; i < n3; i++) {
            temp[i] = sc.nextInt();
        }
        sum = 0;
        for (int i = n3 - 1; i >= 0; i--) {
            sum += temp[i];
            s3.push(sum);
        }

        System.out.println("This is stack1" + s1);
        System.out.println("This is stack2" + s2);
        System.out.println("This is stack3" + s3);

        while (true) {
            if (s1.peek() == s2.peek() && s2.peek() == s3.peek()) {
                System.out.println(s1.peek());
                break;
            } else if (s1.peek() > s2.peek() && s1.peek() > s3.peek()) {
                s1.pop();
            } else if (s2.peek() > s3.peek() && s2.peek() > s1.peek()) {
                s2.pop();
            } else s3.pop();
            if (s1.isEmpty() || s2.isEmpty() || s3.isEmpty()) {
                System.out.println(0);
                break;
            }
        }
    }
}
