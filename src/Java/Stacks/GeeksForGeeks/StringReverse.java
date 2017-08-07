package Java.Stacks.GeeksForGeeks;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * Created by BK on 07-08-2017.
 */
public class StringReverse {
    public static void main(String... strings) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Give a string to reverse it : ");
        String input = reader.readLine();
        reverseStringUsingStack(input);
        System.out.println("String reversed with recursion : ");
        reverseStringUsingRecursion(input, 0);
    }

    private static void reverseStringUsingStack(String input) {
        Stack<Character> stack = new Stack<>();
        System.out.println("String reversed using stack : ");
        for (int i = 0; i < input.length(); i++) stack.push(input.charAt(i));
        while (!stack.isEmpty()) System.out.print(stack.pop());
        System.out.println();
    }

    private static void reverseStringUsingRecursion(String input, int index) {
        if (index < input.length()) {
            reverseStringUsingRecursion(input, index + 1);
            System.out.print(input.charAt(index));
        }
    }
}
