package Project_Euler;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;
import java.util.Scanner;

import static java.lang.Math.floorDiv;
import static java.lang.Math.max;

/**
 * Created by BK on 10-10-2017.
 */
public class LongestCollatzSequence_14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt(), max = 0;
        List<Integer> testCases = new ArrayList<>();
        for (int i_tc = 0; i_tc < tc; i_tc++) {
            int inp = sc.nextInt();
            max = max(inp, max);
            testCases.add(inp);
        }
        Hashtable<Integer, Integer> dict = new Hashtable<>();
        for (int i = 1; i <= max; i += 1) {
            if (!dict.containsKey(i)) collapseThisNumber(i, dict);
        }
        int[] answers = new int[max + 1];
        int current_max = 0, current_answer = 1;
        for (int i = 1; i <= max; i += 1) {
            if (current_max < dict.get(i)) {
                current_max = dict.get(i);
                current_answer = i;
            } else if (current_max == dict.get(i)) current_answer = i;
            answers[i] = current_answer;
        }
        for (Integer testcase : testCases) {
            System.out.println(answers[testcase]);
        }
    }

    private static int collapseThisNumber(Integer testCase, Hashtable<Integer, Integer> dict) {
        if (dict.containsKey(testCase)) return dict.get(testCase);
        else if (testCase == 1) {
            dict.put(1, 0);
            return 0;
        } else if (testCase % 2 == 0) {
            int temp = collapseThisNumber(floorDiv(testCase, 2), dict);
            dict.put(testCase, temp + 1);
            return temp + 1;
        } else {
            int temp = collapseThisNumber(3 * (testCase) + 1, dict);
            dict.put(testCase, temp + 1);
            return temp + 1;
        }
    }
}
