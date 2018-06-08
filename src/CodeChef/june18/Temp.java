package CodeChef.june18;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by bk on 08-06-2018.
 */
class Temp2 {
    int x;

    Temp2(int x) {
        this.x = x;
    }

    Temp2(Temp2 temp2) {
        this.x = temp2.x;
    }

    @Override
    public String toString() {
        return this.x + "";
    }
}

public class Temp {
    public static void main(String[] __) {
        List<Temp2> l = new ArrayList<>();
        Temp2 t = new Temp2(1);
        for (int i = 0; i < 10; i++) {
            t.x = i;
            l.add(new Temp2(t));
        }
        System.out.println(l);
    }
}
