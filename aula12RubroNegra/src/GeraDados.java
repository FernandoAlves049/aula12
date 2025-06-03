import java.io.*;
import java.util.*;

public class GeraDados {
    public static void main(String[] args) throws Exception {
        Random rand = new Random(123);
        try (PrintWriter pw = new PrintWriter(new FileWriter("src/dados100_mil.txt"))) {
            for (int i = 0; i < 100000; i++) {
                int n = rand.nextInt(19999) - 9999;
                pw.println(n);
            }
        }
        System.out.println("Arquivo src/dados100_mil.txt gerado com 100.000 números.");
    }
}
