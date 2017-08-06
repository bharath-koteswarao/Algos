package Java.Stacks.Hackerrank_Problems;

import java.util.Scanner;
import java.util.Stack;

/**
 * Created by BK on 06-08-2017.
 */

public class BalancedParanthesis {
    public static void main(String... strings) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            printAnswer(sc.next());
        }
    }

    private static void printAnswer(String input) {
        Stack<Character> stack = new Stack<>();
        boolean isValid = true;
        for (int i = 0; i < input.length(); i++) {
            char currentChar = input.charAt(i);
            if (currentChar == '{' || currentChar == '(' || currentChar == '[') stack.push(currentChar);
            else if (currentChar == '}') {
                if (stack.isEmpty()) isValid = false;
                else {
                    if (stack.pop() != '{') {
                        isValid = false;
                    }
                }
            } else if (currentChar == ')') {
                if (stack.isEmpty()) isValid = false;
                else {
                    if (stack.pop() != '(') {
                        isValid = false;
                    }
                }
            } else if (currentChar == ']') {
                if (stack.isEmpty()) isValid = false;
                else {
                    if (stack.pop() != '[') {
                        isValid = false;
                    }
                }
            }
        }
        System.out.println(isValid && stack.isEmpty() ? "YES" : "NO");
    }
}