package Java.Stacks;

import java.util.Stack;

/**
 * Created by BK on 05-08-2017.
 */
public class LargestRectangleUnderHistogram {
    public static void main(String... args) {
        int[] input = {6, 2, 5, 4, 5, 1, 6};
        int maxarea = -1;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < input.length; i++) {
            if (stack.isEmpty()) stack.push(i);
            else {
                if (input[stack.peek()] < input[i]) stack.push(i);
                else {

                }
            }
        }
        System.out.println(stack + " " + maxarea);
    }
}
