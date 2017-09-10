package Datastructures.Stacks.GeeksForGeeks;

import Datastructures.bk;

import java.util.Scanner;
import java.util.Stack;

public class NextGreatestElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array : ");
        int n = sc.nextInt();
        int[] inp = bk.getInt(5);
        Stack<Integer> stack = new Stack<>();
        stack.push(inp[0]);
        for (int i = 1; i < inp.length; i++) {
            int element = inp[i];
            if (element > stack.peek()) {
                System.out.println(stack.peek() + " ==> " + element);
                stack.pop();
                while (!stack.isEmpty()) {
                    System.out.println(stack.pop() + " ==> " + element);
                }
                stack.push(element);
            } else if (element < stack.peek()) {
                stack.push(element);
            }
        }
        while (!stack.isEmpty()) System.out.println(stack.pop() + " ==> " + (-1));
    }
}