package Codeforces.Graph;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;

/**
 * Created by bk on 28-05-2018.
 */
public class Vertex {
    public String key;
    public Hashtable<String, Long> neighbors;

    public Vertex(String key) {
        this.key = key;
        neighbors = new Hashtable<>();
    }

    public void addNeighbor(String key, long weight) {
        neighbors.put(key, weight);
    }

    public boolean isNeighbor(String key) {
        return neighbors.containsKey(key);
    }

    public List<String> getNeighbors() {
        return new ArrayList<>(neighbors.keySet());
    }
}
