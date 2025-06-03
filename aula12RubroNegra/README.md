# Projeto: Comparação de Árvores Rubro-Negra e AVL em Java

Este projeto Java compara o desempenho das estruturas de dados Árvore Rubro-Negra (Red-Black Tree) e Árvore AVL, ambas auto-balanceadas, para operações de inserção em massa de dados inteiros.

## Estrutura do Projeto

- `src/`
  - `App.java`: Programa principal. Lê os dados, insere nas árvores, mede tempos e imprime resultados.
  - `AVLTree.java`: Implementação da árvore AVL, com contagem de comparações.
  - `RBTree.java`: Implementação da árvore Rubro-Negra, com contagem de comparações.
  - `GeraDados.java`: Gera automaticamente o arquivo `dados100_mil.txt` com 100.000 números aleatórios.
  - `dados100_mil.txt`: Arquivo de entrada com 100.000 números inteiros (um por linha).
- `bin/`: Arquivos compilados `.class`.
- `gerador_pdf.py`: Script Python para gerar o relatório PDF dos resultados.
- `Relatorio_Desempenho_Arvores.pdf`: Exemplo de relatório gerado.

## Como Executar

1. **Gerar os dados de entrada:**
   ```cmd
   javac -d bin src/GeraDados.java
   java -cp bin GeraDados
   ```
   Isso criará o arquivo `src/dados100_mil.txt`.

2. **Compilar o projeto:**
   ```cmd
   javac -d bin src/*.java
   ```

3. **Executar o experimento:**
   ```cmd
   java -cp bin App
   ```
   O programa irá mostrar os tempos de inserção e o número de comparações para cada árvore.

4. **Gerar o relatório PDF (opcional):**
   - Edite os valores no início de `gerador_pdf.py` com os resultados do seu experimento.
   - Execute:
     ```cmd
     python gerador_pdf.py
     ```
   - O arquivo `Relatorio_Desempenho_Arvores.pdf` será gerado.

## Sobre as Árvores

- **AVLTree.java:** Mantém balanceamento estrito, garantindo altura próxima de log₂(n). Ideal para buscas rápidas.
- **RBTree.java:** Balanceamento mais flexível, geralmente exige menos rotações em inserções e remoções. Costuma ser mais eficiente para grandes volumes de inserção/remoção.

## Observações

- Os tempos de execução podem variar a cada execução devido ao ambiente do sistema.
- O projeto é didático e pode ser expandido para outros testes ou visualizações.

---

Desenvolvido para fins acadêmicos. Para dúvidas ou sugestões, entre em contato.
