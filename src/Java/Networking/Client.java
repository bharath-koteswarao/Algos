package Java.Networking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;

/**
 * Created by BK on 23-08-2017.
 */
public class Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 5555);
            PrintStream stream = new PrintStream(socket.getOutputStream());
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(socket.getInputStream())
            );
            System.out.println(reader.readLine());
            socket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}