package Datastructures.Networking;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

/**
 * Created by BK on 23-08-2017.
 */
public class Server {
    public static void main(String[] args) throws IOException {
        System.out.println("Waiting for connections...");
        Scanner sc = new Scanner(System.in);
        ServerSocket serverSocket = new ServerSocket(5555);
        Socket socket = serverSocket.accept();
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
        boolean done = false;
        while (!done) {
            System.out.print("Send : ");
            String data = sc.next();
            send(dos, data);
            System.out.println("Done ? : Y or N");
            done = sc.next().equals("Y");
        }
    }

    static void send(DataOutputStream dos, String data) throws IOException {
        dos.writeByte(0);
        dos.writeUTF(data);
        dos.flush();
    }

}