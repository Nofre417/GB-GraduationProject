import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        ToyQueue toyQueue = new ToyQueue();

        // Добавим игрушки в очередь
        toyQueue.addToQueue(new Toy(1, "Constructor", 2));
        toyQueue.addToQueue(new Toy(2, "Robot", 2));
        toyQueue.addToQueue(new Toy(3, "Doll", 6));

        try {
            Repository.Save(toyQueue);
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public static String getToyNameById(int toyId) {
        switch (toyId) {
            case 1:
                return "Constructor";
            case 2:
                return "Robot";
            case 3:
                return "Doll";
            default:
                return "Unknown toy";
        }
    }
}