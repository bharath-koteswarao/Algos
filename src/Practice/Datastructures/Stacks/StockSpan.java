package Datastructures.Stacks;

import Datastructures.bk;

import java.util.Stack;

/**
 * Created by BK on 03-08-2017.
 */
public class StockSpan {

    static int[] getInput(int... args) {
        return args;
    }

    public static void main(String... args) {

        // Stack is used for holding the indices

        Stack<Integer> stack = new Stack();
        int[] input = getInput(6, 3, 4, 5, 2);
        int[] spans = new int[input.length];

        //  First Element of spans is always 1 since there is no element to left of it

        spans[0] = 1;
        for (int i = 0; i < input.length; i++) {

            /*
            *   For all elements in the input do the following :
            *   if the current element (i) is greater than input[ top element of stack]
            *   then pop until it becomes less than input[ top element of stack]
            *   From this we get the first preceding number greater than this current element
            *   Now we have first preceding largest number greater than current
            *   number as the top of the stack
            * */

            while (!stack.isEmpty() && input[i] >= input[stack.peek()]) {
                stack.pop();
            }

            /*
            *   If stack is empty it means that all elements to left
            *   of the current element are smaller than current element
            *   So the span of this element becomes its index+1
            *   Now push i into stack
            * */

            if (stack.isEmpty()) {
                spans[i] = i + 1;
                stack.push(i);
            }
            /*
            *   If stack is not empty then we have first large number to left of this
            *
            * */

            else {
                spans[i] = i - stack.peek();
                stack.push(i);
            }
        }
        bk.print_int(spans);
    }
}
