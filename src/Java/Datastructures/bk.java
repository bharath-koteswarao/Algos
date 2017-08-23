package Java.Datastructures;

import java.util.Scanner;

public class bk {
    static Scanner takeInput = new Scanner(System.in);
    private static int i = 0;

    public static void print_int(int arr[]) {
        for (i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " " + "|" + " ");
        }
        System.out.println();
    }

    public static void print_boolenas(boolean arr[]) {
        for (i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " " + "|" + " ");
        }
        System.out.println();
    }

    public static void print_float(float arr[]) {
        for (i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " " + "|" + " ");
        }
        System.out.println();
    }

    public static void print_string(String arr[]) {
        for (i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " " + "|" + " ");
        }
        System.out.println();
    }

    public static void print_double(double arr[]) {
        for (i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " " + "|" + " ");
        }
        System.out.println();
    }

    public static void print_long(long arr[]) {
        for (i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " " + "|" + " ");
        }
        System.out.println();
    }

    public static void sop(Object obj) {
        System.out.print(obj + " ");
    }

    public static void sopln(Object obj) {
        System.out.println(obj);
    }

    public static int[] getInt(int arraySize) {
        int arrayToReturn[] = new int[arraySize];
        for (i = 0; i < arraySize; i++) {
            arrayToReturn[i] = takeInput.nextInt();
        }
        return arrayToReturn;
    }

    public static String[] getString(int arraySize) {
        String arrayToReturn[] = new String[arraySize];
        for (i = 0; i < arraySize; i++) {
            arrayToReturn[i] = takeInput.next();
        }
        return arrayToReturn;
    }

    public static float[] getFloat(int arraySize) {
        float arrayToReturn[] = new float[arraySize];
        for (i = 0; i < arraySize; i++) {
            arrayToReturn[i] = takeInput.nextFloat();
        }
        print_float(arrayToReturn);
        System.out.println("done ;)");
        return arrayToReturn;
    }

    public static long[] getLong(int arraySize) {
        long arrayToReturn[] = new long[arraySize];
        for (i = 0; i < arraySize; i++) {
            arrayToReturn[i] = takeInput.nextLong();
        }
        print_long(arrayToReturn);
        System.out.println("done ;)");
        return arrayToReturn;
    }

    public static double[] getDouble(int arraySize) {
        double arrayToReturn[] = new double[arraySize];
        for (i = 0; i < arraySize; i++) {
            arrayToReturn[i] = takeInput.nextDouble();
        }
        print_double(arrayToReturn);
        System.out.println("done ;)");
        return arrayToReturn;
    }
}
