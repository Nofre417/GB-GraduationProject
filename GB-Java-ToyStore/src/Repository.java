import java.io.FileWriter;
import java.io.IOException;

public class Repository {
    public static void Save(ToyQueue toyQueue) throws IOException{
        try (FileWriter writer = new FileWriter("ToyStore.txt")) {
            for (int i = 0; i < 10; i++) {
                int toyId = toyQueue.getToy();
                writer.write("Get result: " + toyId + " - " + Main.getToyNameById(toyId) + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
