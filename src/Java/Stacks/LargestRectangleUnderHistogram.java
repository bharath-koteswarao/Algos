package Java.Stacks;

import java.util.Scanner;
import java.util.Stack;

/**
 * Created by BK on 05-08-2017.
 */
public class LargestRectangleUnderHistogram {
    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] input = new int[n];
        for (int j = 0; j < n; j++) {
            input[j] = scanner.nextInt();
        }



        /*
        *   This is the procedure used for solving :
        *
        *   Travel from first element to last element of the array
        *
        *   If stack is empty add current element to stack
        *
        *   If stack is not empty check for the top element of stack if
        *   it is smaller than the current element push into stack
        *
        *   If it is larger than the current element pop the stack until we get an
        *   element smaller than the current element or until stack becomes empty
        *
        *   After popping each element check if the stack is empty or not..
        *
        *   If stack is empty it means that this is the smallest element encountered till now
        *
        *   So we can multiply i with this element to get a big rectangle which is contributed by
        *
        *   this
        *
        *   If stack is not empty then check for individual areas(Not just one bar individual area means largest rectangle by this) (i-top)*input[top]
        *
        *
        * */

        /*
        * Initializing the maxarea as we check each area with maxarea
        */

        int maxarea = -1;
        int i;
        Stack<Integer> stack = new Stack<>();
        for (i = 0; i < input.length; i++) {

            /*
            *   Pushing the element if stack is empty
            * */


            if (stack.isEmpty()) {
                stack.push(i);
            } else {

                /*
                *   If stack top element is less than current element push
                * */

                if (input[stack.peek()] < input[i]) {
                    stack.push(i);
                } else {

                    /*
                    *   Else pop until we encounter an element smaller than this in stack or stack becomes empty
                    *
                    * */


                    while (!stack.isEmpty() && input[stack.peek()] > input[i]) {

                        int top = stack.pop();

                        /*
                        *   If stack is empty means this is the smallest element encountered so far
                        *
                        *   So we can multiply this with i
                        * */

                        if (stack.isEmpty()) {
                            maxarea = maxarea < (input[top] * i) ? (input[top] * i) : maxarea;
                        }

                        /*
                         *  If stack is not empty we find areas of each individual rectangle
                         *  Remember we are in while loop
                         */

                        else {
                            maxarea = maxarea < (input[top] * (i - top)) ? (input[top] * (i - top)) : maxarea;
                        }
                    }
                    /*
                    *   Finally pushing the current element to stack
                    * */

                    stack.push(i);
                }
            }
        }

        /*
        *  This is for checking if stack is not empty after looping the last element of input
        *
        *  This happens if input is like this 4 5 6 1 2 3 4 5
        *
        *  Here 2 3 4 5 remains in stack as they are always increasing and we never got
        *
        *  a chance to pop them from stack by above process
        *
        * */


        while (!stack.isEmpty()) {

            int top = stack.pop();

            if (stack.isEmpty()) {
                maxarea = Math.max(maxarea, (i - top) * input[top]);
            } else {

                /*
                *
                *     To understand why stack.peek()-1 in  (i - stack.peek() - 1) is written
                *
                *     Just Consider this example :
                *
                *     Number of inputs : 4
                *
                *     1 5 6 4 After the above for loop terminates i becomes 5
                *
                *     Here 1 and 5 and 6 gets pushed into stack (indices)
                *     When 4 comes every thing is popped  except 1(index 0) as it is smaller than 4
                *     So we need to multiply 4 by 3 times
                *     We obtain this 3 by doing i-current top of stack-1
                *     This is the reason why (i - stack.peek() - 1) is written.
                * */

                maxarea = Math.max(maxarea, (i - stack.peek() - 1) * input[top]);
            }
        }

        System.out.println(maxarea);
    }
}
