package Hackerrank.week_of_code_36;

/*
 * Created by bk on 08-02-2018 19:11
 */

/*
4
5
2 6 2
2 3 2

7
3
2 6 7 1 2 3
1 -2 3 -4 5 1
 */

import java.util.Arrays;
import java.util.Scanner;

class Player {
    public long height, price;
    int index;

    Player() {
    }

    Player(long height, long price, int index) {
        this.height = height;
        this.price = price;
    }

    @Override
    public String toString() {
        return "(" + this.height + ", " + this.price + ")";
    }
}

public class RaceAgainstTime {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long mason = sc.nextLong();
        Player[] players = new Player[n];
        players[0] = new Player(mason, 0, 0);
        for (int i = 1; i < n; i++) {
            players[i] = new Player();
            players[i].height = sc.nextLong();
            players[i].index = i;
        }
        for (int i = 1; i < n; i++) {
            players[i].price = sc.nextLong();
        }
        int[] maxHeight = new int[n];
        long temp = 0;
        int max = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (players[i].height > temp) {
                max = i;
                temp = players[i].height;
            }
            maxHeight[i] = max;
        }
        System.out.println(Arrays.toString(maxHeight));
        long cost = 0;
        Player target = players[players.length - 1];
        int minIndex = n - 2;
        while (minIndex != 0) {
            long tempCost = Integer.MAX_VALUE;
            for (int i = minIndex; i >= 0; i--) {
                if (maxHeight[i] == i || maxHeight[i] == target.index) {

                } else {

                }
            }
        }
    }
}
