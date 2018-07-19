package transtutors.id_2748343;

import java.math.BigInteger;

public class given {
    public static void main(String[] args) {
        System.out.println(theBigFib(100));
    }

    // This is used to call the function with integer argument
    public static BigInteger theBigFib(int n) {
        // calling the "theBigFib" function which returns BigInteger
        return theBigFib(BigInteger.valueOf(n));
    }

    // This is used to call the function with BigInteger argument
    public static BigInteger theBigFib(BigInteger n) {
        // Declaring a BigInteger array for memoization purpose
        BigInteger[] memo = new BigInteger[n.intValue() + 1];
        // Initializing the first two values of memo
        memo[0] = BigInteger.valueOf(0);
        memo[1] = BigInteger.ONE;
        // Initializing the remaining values to -1 so that we can check if this value was calculated before
        for (int i = 2; i < memo.length; i++) memo[i] = BigInteger.valueOf(-1);
        // Calling the helper function
        return getBigFib(n, memo);
    }


    // The recursive helper function
    public static BigInteger getBigFib(BigInteger n, BigInteger[] memo) {
        // First check if this value has been calculated earlier or not
        if (memo[n.intValue()].equals(BigInteger.valueOf(-1))) {
            // If we are in this block the value was not calculated earlier
            // So we need to calculate it and store it in memo
            if (n.equals(BigInteger.valueOf(0))) return BigInteger.valueOf(0);
            else if (n.equals(BigInteger.valueOf(1))) return BigInteger.valueOf(1);
            else {
                // Storing the calculated value in memo
                memo[n.intValue()] = getBigFib(n.subtract(BigInteger.ONE), memo).add(getBigFib(n.subtract(BigInteger.TWO), memo));
                // Returning the same
                return memo[n.intValue()];
            }
        } // If already calculated return the value from memo
        else return memo[n.intValue()];
    }
}