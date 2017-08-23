package Datastructures.Stacks.Hackerrank_Problems;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by BK on 09-08-2017.
 */
public class GameOfTwoStacksImproved {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int z = 0; z < tc; z++) {
            int size1 = sc.nextInt();
            int size2 = sc.nextInt();
            int x = sc.nextInt();
            ArrayList<Integer> list1 = new ArrayList<>(), list2 = new ArrayList<>();
            int[] sums1 = new int[size1], sums2 = new int[size2];
            int temp = 0;
            for (int i = 0; i < size1; i++) {
                list1.add(sc.nextInt());
                temp += list1.get(i);
                sums1[i] = temp;
            }
            temp = 0;
            for (int i = 0; i < size2; i++) {
                list2.add(sc.nextInt());
                temp += list2.get(i);
                sums2[i] = temp;
            }
//            System.out.println(list1 + " " + list2);
//            bk.print_int(sums1);
//            bk.print_int(sums2);
            while (sums1[size1 - 1] > x) {
                list1.remove(size1 - 1);
                size1--;
            }
            while (sums2[size2 - 1] > x) {
                list2.remove(size2 - 1);
                size2--;
            }
            int n1 = list1.size() - 1, n2 = list2.size() - 1;

            int sum = sums1[n1] + sums2[n2];
            while (n1 >= 0 && n2 >= 0 && sum > x) {
                if (list1.get(n1) > list2.get(n2)) {
                    sum -= list1.get(n1);
                    list1.remove(n1);
                    n1--;
                } else if (list1.get(n1) < list2.get(n2)) {
                    sum -= list2.get(n2);
                    list2.remove(n2);
                    n2--;
                } else {
                    n1--;
                    n2--;
                }
            }

            System.out.println(list1.size() + list2.size());
        }
    }
}
