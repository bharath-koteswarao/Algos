//package Networking;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * Created by BK on 23-08-2017.
 */
public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 5555);
        DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
        while (dataInputStream.readByte() == 0) {
            System.out.println(dataInputStream.readUTF());
        }
    }
}