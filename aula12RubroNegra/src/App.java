import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) {
        String nomeArquivo = "src/dados100_mil.txt";
        System.out.println("Iniciando processamento com o arquivo: " + nomeArquivo);
        System.out.println("--------------------------------------------------");

        List<Integer> numeros = new ArrayList<>();
        int linhasIgnoradas = 0;

        // --- Fase 1: Leitura do Arquivo ---
        System.out.println("Fase 1: Lendo os dados do arquivo...");
        long startTimeLeitura = System.nanoTime();
        try {
            Path caminho = Paths.get(nomeArquivo);
            BufferedReader leitor = Files.newBufferedReader(caminho);
            String linha;
            while ((linha = leitor.readLine()) != null) {
                try {
                    numeros.add(Integer.parseInt(linha.trim()));
                } catch (NumberFormatException e) {
                    linhasIgnoradas++;
                }
            }
            leitor.close();
        } catch (IOException e) {
            System.err.println("Erro fatal ao ler o arquivo '" + nomeArquivo + "': " + e.getMessage());
            e.printStackTrace();
            return;
        }
        long endTimeLeitura = System.nanoTime();
        long durationLeituraMs = (endTimeLeitura - startTimeLeitura) / 1_000_000;
        System.out.println("Leitura do arquivo concluída em " + durationLeituraMs + " ms.");
        System.out.println(numeros.size() + " números lidos com sucesso.");
        if (linhasIgnoradas > 0) {
            System.out.println(linhasIgnoradas + " linhas foram ignoradas (não numéricas).");
        }
        System.out.println("--------------------------------------------------");

        if (numeros.isEmpty()) {
            System.out.println("Nenhum número foi lido do arquivo. Encerrando.");
            return;
        }

        // --- Fase 2: Teste com Árvore Rubro-Negra ---
        System.out.println("Fase 2: Processando com Árvore Rubro-Negra...");
        RBTree arvoreRubroNegra = new RBTree();
        long startTimeRB = System.nanoTime();
        for (int numero : numeros) {
            arvoreRubroNegra.insert(numero);
        }
        long endTimeRB = System.nanoTime();
        long durationRBMs = (endTimeRB - startTimeRB) / 1_000_000;
        System.out.println("Inserção na Árvore Rubro-Negra concluída.");
        System.out.println("Tempo de inserção para Rubro-Negra: " + durationRBMs + " ms");
        System.out.println("Comparações Rubro-Negra: " + arvoreRubroNegra.getComparisons());
        System.out.println("--------------------------------------------------");

        // --- Fase 3: Teste com Árvore AVL ---
        System.out.println("Fase 3: Processando com Árvore AVL...");
        AVLTree arvoreAVL = new AVLTree();
        long startTimeAVL = System.nanoTime();
        for (int numero : numeros) {
            arvoreAVL.insert(numero);
        }
        long endTimeAVL = System.nanoTime();
        long durationAVLMs = (endTimeAVL - startTimeAVL) / 1_000_000;
        System.out.println("Inserção na Árvore AVL concluída.");
        System.out.println("Tempo de inserção para AVL: " + durationAVLMs + " ms");
        System.out.println("Comparações AVL: " + arvoreAVL.getComparisons());
        System.out.println("--------------------------------------------------");

        // --- Fase 4: Comparativo dos Tempos de Inserção ---
        System.out.println("Fase 4: Comparativo dos Tempos de Inserção");
        System.out.println("Tempo de Inserção (Rubro-Negra): " + durationRBMs + " ms");
        System.out.println("Tempo de Inserção (AVL):         " + durationAVLMs + " ms");
        if (durationRBMs > 0 && durationAVLMs > 0) {
            if (durationRBMs < durationAVLMs) {
                System.out.println("A Árvore Rubro-Negra foi mais rápida na inserção para este conjunto de dados.");
            } else if (durationAVLMs < durationRBMs) {
                System.out.println("A Árvore AVL foi mais rápida na inserção para este conjunto de dados.");
            } else {
                System.out.println("Os tempos de inserção foram equivalentes para este conjunto de dados.");
            }
        }
        System.out.println("--------------------------------------------------");
        System.out.println("\nExecução do App finalizada.");
    }
}