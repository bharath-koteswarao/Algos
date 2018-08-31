package SystemDesign.parkingLot;

/**
 * Created by bk on 31-08-2018.
 */

enum size {
    SMALL, MEDIUM, LARGE
}

abstract class Vehicle {
    private size size;

    Vehicle(size size) {
        this.size = size;
    }

    public size getSize() {
        return size;
    }
}

class Car extends Vehicle {

    Car(SystemDesign.parkingLot.size size) {
        super(size);
    }
}

class ParkingLot {
    private int levels;
    private int lastUsedLevel = 0;
    private int lastUsedRow = 0;
    private boolean[][] spots;

    ParkingLot(int levels) {
        this.levels = levels;
        spots = new boolean[this.levels][10];
    }

    public void park(Vehicle vehicle) {
        size cur = vehicle.getSize();
        if (cur == size.MEDIUM) {
            if (10 - (lastUsedRow + 1) >= 2) {
                for (int i = 0; i < 2; i++) {
                    spots[lastUsedLevel][lastUsedRow] = true;
                    lastUsedRow += 1;
                }
                printPlace(lastUsedLevel, lastUsedRow - 2);
            } else {
                lastUsedLevel += 1;
                lastUsedRow = 0;
                for (int i = 0; i < 2; i++) {
                    spots[lastUsedLevel][lastUsedRow] = true;
                    lastUsedRow += 1;
                }
                printPlace(lastUsedLevel, lastUsedRow - 2);
            }
        }
    }

    private void printPlace(int lastUsedLevel, int j) {
        System.out.println("Vehicle can be parked at " + lastUsedLevel + " floor " + j + " place");
    }
}

public class Main {
    public static void main(String[] __) {
        Car car = new Car(size.MEDIUM);
        ParkingLot pl = new ParkingLot(10);
        for (int i = 0; i < 10; i++) {
            pl.park(car);
        }
    }
}