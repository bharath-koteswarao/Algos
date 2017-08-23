package Java.Networking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by BK on 23-08-2017.
 */
public class Server {
    public static void main(String[] args) {
        System.out.println("Waiting for connections...");
        PrintStream writer;
        BufferedReader reader;
        try {
            ServerSocket serverSocket = new ServerSocket(5555);
            Socket socket = serverSocket.accept();
            System.out.println("Connected...");
            writer = new PrintStream(socket.getOutputStream());
            reader = new BufferedReader(
                    new InputStreamReader(socket.getInputStream())
            );
            writer.print("Hello");
            reader.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}