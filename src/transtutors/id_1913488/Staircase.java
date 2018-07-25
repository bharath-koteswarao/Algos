
import java.util.Hashtable;
import java.util.Scanner;

/**
 * Created by bharath on 25-07-2018.
 */

/*
 * This is a classic problem in which dynamic programming has to be applied with the help of an array
 * I would like to extend this problem for climbing n number of steps at a time :)
 * With just 1 or two steps at a time it is too simple :)
 */
public class Staircase {

    public static void main(String[] args) {
        // Scanner for reading input
        Scanner sc = new Scanner(System.in);

        // basically this is for storing the solution of the sub problems which were already computed
        Hashtable<Long, Long> memo = new Hashtable<>();

        // This is one of the base conditions for our recurrence relation. Don't confuse why we have taken 1 for 0.
        // I explained it below :)
        memo.put(0L, 1L);

        // Reading the input
        long n = sc.nextLong();

        // Yeah you can extend to n steps by just adding n to this array
        // For example if you want to calculate the number of ways of climbing n stairs where you can climb 1 or 2 or 3 steps at a time simply add 3 to array
        // so just int[] arr = {1, 2, 3} would suffice for above condition. Just give it a try :)
        int[] arr = {1, 2};

        // This is basically calling the function to get answer
        long ans = ways(n, arr, memo);
        System.out.println(ans);
    }

    private static long ways(long n, int[] arr, Hashtable<Long, Long> memo) {
        if (memo.containsKey(n)) {
            // Just check if this problem was already calculated. If it was calculated already then we can simply use the earlier result.
            return memo.get(n);
        }
        else {
            if (n == 0) {

                // Yeah if n is 0 we could simply stay there without doing anything and still we finished the task of climbing 0 stairs. So answer is 1 if n is 0
                return 1;
            } else if (n <= 0) {

                // Too obvious to explain
                return 0;
            } else {
                long ans = 0;

                // This is the tricky part. I will explain this by taking arr = {1, 2}
                // So for example n = 5 and arr = {1, 2} means we can only climb one or two steps at a time. Your question :)
                // Common sense is saying that number of ways for 5 is number of ways for (5 - 1 = 4) + (5 - 2 = 3)
                // Again number of ways for 4 is number of ways for (4 - 1 = 3) + (4 - 2 = 2)
                // Similarly we recur until we reach zero !! As simple as that
                // Have you noticed that we calculated number of ways for 3 2 times ?? That's the exact time when memo comes to picture
                for (int i : arr) ans += ways(n - i, arr, memo);
                memo.put(n, ans);
                return ans;
            }
        }
    } // Hope you understood it.

    // Since first and second are not related questions I'm answering only the first one. You might have to post the second one as a separate question
}
