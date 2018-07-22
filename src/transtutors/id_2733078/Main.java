package transtutors.id_2733078;

class stack {
    private int[] data;
    private int top;
    private int size;

    public stack() {
        top = -1;
        size = 100;
        data = new int[100];
    }

    public stack(int n) {
        top = -1;
        size = n;
        data = new int[n];
    }

    public boolean push(int n) {
        if (top == size - 1) return false;
        else {
            data[++top] = n;
            return true;
        }
    }

    public int pop() {
        if (top == -1) return -1;
        else return data[top--];
    }

    public void showAll() {
        for (int element: data) System.out.println(element);
    }

    public void makeStackEmpty() {
        data = new int[size];
        top = -1;
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == size - 1;
    }

    public int peek() {
        return data[top];
    }
}

public class Main {
    public static void main(String[] __) {
        stack s = new stack(10);

        s.push(1);
        s.push(2);
        s.push(3);

        // Implementing newly created methods

        s.makeStackEmpty(); // Makes the stack empty

        System.out.println(s.isEmpty()); // Prints true

        System.out.println(s.isFull()); // prints false

        s.push(10);

        System.out.println(s.peek()); // prints 10


    }
}