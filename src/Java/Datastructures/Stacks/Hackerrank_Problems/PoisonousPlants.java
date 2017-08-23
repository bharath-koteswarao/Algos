package Datastructures.Stacks.Hackerrank_Problems;

import java.util.Scanner;

public class PoisonousPlants {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] inputs = new int[n];
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            inputs[i] = sc.nextInt();
        }
        int min = inputs[0];
        for (int i = 1; i < inputs.length; i++) {
            min = Math.min(inputs[i], min);
            if (inputs[i] > inputs[i - 1]) {
                answer[i] = answer[i] + 1;
            } else {
                if (inputs[i] == min) answer[i] = 0;
                else answer[i] = answer[i - 1] + 1;
            }
        }
        int max = -1;
        for (int i = 0; i < answer.length; i++) {
            max = Math.max(max, answer[i]);
        }
        System.out.println(max);
    }
}
