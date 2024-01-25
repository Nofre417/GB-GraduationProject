import java.util.PriorityQueue;

public class ToyQueue {
    private PriorityQueue<Toy> toyPriorityQueue;

    public ToyQueue() {
        toyPriorityQueue = new PriorityQueue<>((t1, t2) -> Integer.compare(t2.getFrequency(), t1.getFrequency()));
    }

    public void addToQueue(Toy toy) {
        toyPriorityQueue.add(toy);
    }

    public int getToy() {
        int random = (int) (Math.random() * 100);
        if (random < 20) {
            return 1;
        } else if (random < 40) {
            return 2;
        } else {
            return 3;
        }
    }
}