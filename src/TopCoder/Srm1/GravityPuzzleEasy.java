package TopCoder.Srm1;

/*
 * Created by bk on 28-11-2017 21:46
 */

public class GravityPuzzleEasy {
    public static void main(String[] args) {
        String[] inp = {"..#.#",
                "#.#..",
                "...##"};
        String[] a = solve(inp);
    }

    public static String[] solve(String[] board) {
        char[][] inp = new char[board.length][board[0].length()];
        for (int i = 0; i < board.length; i++) {
            inp[i] = board[i].toCharArray();
        }
        int[] count = new int[board[0].length()];
        for (int i = 0; i < board[0].length(); i++) {
            for (int j = 0; j < board.length; j++) {
                if (inp[j][i] == '#') count[i] += 1;
            }
        }

        for (int i = 0; i < count.length; i++) {
            count[i] = board.length - count[i];
        }
        String[] op = new String[board.length];
        for (int i = 0; i < board[0].length(); i++) {
            for (int j = 0; j < board.length; j++) {
                if (count[i] > 0) {
                    inp[j][i] = '.';
                    count[i] -= 1;
                } else {
                    inp[j][i] = '#';
                }
            }
        }
        for (int i = 0; i < board.length; i++) {
            String temp = "";
            for (int j = 0; j < board[0].length(); j++) {
                temp += inp[i][j];
            }
            op[i] = temp;
        }
        return op;
    }
}
