from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepInFrame, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.units import cm
from reportlab.lib.colors import navy, black

def gerar_pdf_relatorio(nome_arquivo_pdf="Relatorio_Desempenho_Arvores.pdf"):
    # --- DADOS DA EXECUÇÃO DO SEU PROGRAMA JAVA ---
    # !!! ATENÇÃO: MODIFIQUE OS VALORES ABAIXO COM OS RESULTADOS REAIS !!!
    NUMERO_ELEMENTOS_LIDOS = "100000"  # Ex: "100000" ou o número exato de elementos processados
    TEMPO_RB_MS = "38"  # Ex: "1234" (apenas o número, a unidade 'ms' será adicionada no texto)
    TEMPO_AVL_MS = "37"  # Ex: "987"
    NUMERO_COMPARACOES_RB = "1964021"  # Ex: "123456"
    NUMERO_COMPARACOES_AVL = "1950177"  # Ex: "234567"
    
    # (Opcional) Personalize a interpretação dos resultados aqui se desejar
    interpretacao_resultados_personalizada = (
        f"Nos testes realizados, a Árvore Rubro-Negra apresentou um tempo de inserção de {TEMPO_RB_MS} ms, "
        f"enquanto a Árvore AVL levou {TEMPO_AVL_MS} ms. "
        # Adicione sua análise aqui
    )
    # --- FIM DOS DADOS MODIFICÁVEIS ---

    doc = SimpleDocTemplate(nome_arquivo_pdf, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()

    # Estilos personalizados
    styles.add(ParagraphStyle(name='TituloPrincipal',
                              fontName='Helvetica-Bold',
                              fontSize=16,
                              leading=20,
                              alignment=TA_CENTER,
                              spaceAfter=0.8*cm,
                              textColor=navy))

    styles.add(ParagraphStyle(name='CabecalhoSecao',
                              fontName='Helvetica-Bold',
                              fontSize=12,
                              leading=14,
                              spaceBefore=0.6*cm,
                              spaceAfter=0.3*cm,
                              textColor=black))

    styles.add(ParagraphStyle(name='CorpoTexto',
                              parent=styles['Normal'],
                              alignment=TA_JUSTIFY,
                              spaceAfter=0.2*cm,
                              leading=14))

    styles.add(ParagraphStyle(name='ListItem',
                              parent=styles['Normal'],
                              alignment=TA_LEFT,
                              leftIndent=0.5*cm,
                              spaceAfter=0.1*cm,
                              leading=14))

    story = []

    # Título
    story.append(Paragraph("Relatório de Comparação de Desempenho: Árvore Rubro-Negra vs. Árvore AVL", styles['TituloPrincipal']))

    # --- BREVE EXPLICAÇÃO DOS ARQUIVOS DO PROJETO ---
    story.append(Paragraph("Arquivos do Projeto", styles['CabecalhoSecao']))
    explicacoes = [
        ("App.java", "Arquivo principal que executa o experimento, realiza a leitura dos dados, insere nas árvores, mede os tempos e imprime os resultados."),
        ("AVLTree.java", "Implementação da árvore AVL, incluindo métodos de inserção, remoção, contagem e contagem de comparações."),
        ("RBTree.java", "Implementação da árvore Rubro-Negra, incluindo métodos de inserção, remoção, contagem e contagem de comparações."),
        ("dados100_mil.txt", "Arquivo de texto contendo 100.000 números inteiros (um por linha) utilizados como dados de entrada para os testes."),
        ("GeraDados.java", "Programa auxiliar que gera automaticamente o arquivo dados100_mil.txt com 100.000 números aleatórios.")
    ]
    for nome, desc in explicacoes:
        story.append(Paragraph(f"<b>{nome}</b>: {desc}", styles['ListItem']))

    # --- EXEMPLOS DE USO DOS ARQUIVOS ---
    story.append(Paragraph("Exemplos de Uso dos Arquivos", styles['CabecalhoSecao']))
    exemplos = [
        ("App.java", "Para executar o experimento e obter os resultados, compile e execute este arquivo após garantir que os demais arquivos necessários estão presentes."),
        ("GeraDados.java", "Execute este arquivo para gerar automaticamente o arquivo de dados de entrada (dados100_mil.txt) com 100.000 números aleatórios."),
        ("dados100_mil.txt", "Este arquivo é utilizado como entrada pelo App.java. Certifique-se de que ele está no local correto antes de rodar o experimento."),
        ("AVLTree.java / RBTree.java", "Esses arquivos são utilizados pelo App.java para criar, inserir e medir o desempenho das árvores AVL e Rubro-Negra, respectivamente.")
    ]
    for nome, exemplo in exemplos:
        story.append(Paragraph(f"<b>{nome}</b>: {exemplo}", styles['ListItem']))

    # 2. Metodologia
    story.append(Paragraph("2. Metodologia", styles['CabecalhoSecao']))
    texto_metodologia = (
        f"Os dados foram lidos do arquivo <code>dados100_mil.txt</code>. O mesmo conjunto de dados e a "
        f"mesma ordem de inserção foram utilizados para ambas as árvores para garantir uma comparação justa. "
        f"As implementações das árvores utilizadas foram desenvolvidas como parte da atividade acadêmica. "
        f"O tempo foi medido utilizando o método <code>System.nanoTime()</code> do Java para maior precisão, "
        f"cobrindo apenas a operação de inserção dos elementos na estrutura de dados, após a leitura "
        f"completa do arquivo."
    )
    story.append(Paragraph(texto_metodologia, styles['CorpoTexto']))

    # 3. Resultados dos Tempos de Execução (Inserção)
    story.append(Paragraph("3. Resultados dos Tempos de Execução (Inserção)", styles['CabecalhoSecao']))
    texto_resultados = (
        f"Após a execução do programa Java, os seguintes tempos foram observados para a inserção de "
        f"{NUMERO_ELEMENTOS_LIDOS} elementos:"
    )
    story.append(Paragraph(texto_resultados, styles['CorpoTexto']))
    story.append(Paragraph(f"&bull; Tempo de Inserção na Árvore Rubro-Negra: <b>{TEMPO_RB_MS} ms</b>", styles['ListItem']))
    story.append(Paragraph(f"&bull; Tempo de Inserção na Árvore AVL: <b>{TEMPO_AVL_MS} ms</b>", styles['ListItem']))
    story.append(Paragraph(f"&bull; Comparações na Árvore Rubro-Negra: <b>{NUMERO_COMPARACOES_RB}</b>", styles['ListItem']))
    story.append(Paragraph(f"&bull; Comparações na Árvore AVL: <b>{NUMERO_COMPARACOES_AVL}</b>", styles['ListItem']))

    # 4. Análise Comparativa Teórica e Prática
    story.append(Paragraph("4. Análise Comparativa Teórica e Prática", styles['CabecalhoSecao']))

    story.append(Paragraph("4.1. Árvore AVL", styles['CabecalhoSecao']))
    texto_avl = (
        "<b>Balanceamento:</b> As Árvores AVL são as árvores de busca binária auto-balanceadas mais antigas. "
        "Elas mantêm um balanceamento estrito: para qualquer nó, as alturas de suas duas subárvores "
        "filhas podem diferir em no máximo 1.<br/><br/>"
        "<b>Consequências do Balanceamento Estrito:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <i>Busca:</i> Devido ao balanceamento rigoroso, a altura de uma árvore AVL é minimamente "
        "próxima de log₂(n). Isso tende a resultar em operações de busca muito rápidas.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <i>Inserção e Remoção:</i> Para manter o critério de balanceamento estrito, as operações "
        "podem exigir um número maior de rotações. Cada operação tem complexidade O(log n), mas a "
        "constante pode ser um pouco maior devido às rotações."
    )
    story.append(Paragraph(texto_avl, styles['CorpoTexto']))

    story.append(Paragraph("4.2. Árvore Rubro-Negra (Red-Black Tree)", styles['CabecalhoSecao']))
    texto_rb = (
        "<b>Balanceamento:</b> As Árvores Rubro-Negras também garantem O(log n) para todas as operações, "
        "mas suas regras de balanceamento são um pouco menos estritas. Elas usam propriedades de "
        "coloração (cada nó é vermelho ou preto) para garantir que o caminho mais longo da raiz a uma "
        "folha não seja mais do que duas vezes o caminho mais curto.<br/><br/>"
        "<b>Consequências do Balanceamento Menos Estrito:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <i>Busca:</i> A altura de uma árvore Rubro-Negra pode ser um pouco maior que a de uma AVL "
        "(até aproximadamente 2*log₂(n)), podendo levar a tempos de busca ligeiramente mais lentos.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <i>Inserção e Remoção:</i> Geralmente exigem menos rotações do que em AVLs. O número máximo de "
        "rotações para uma inserção é 2, e para uma remoção é 3. As operações de rebalanceamento "
        "são geralmente mais rápidas, o que pode tornar a inserção e remoção mais eficientes."
    )
    story.append(Paragraph(texto_rb, styles['CorpoTexto']))

    story.append(Paragraph("4.3. Comparação com os Resultados Obtidos", styles['CabecalhoSecao']))
    story.append(Paragraph(interpretacao_resultados_personalizada, styles['CorpoTexto']))
    texto_consideracoes = (
        "É importante notar que a performance real pode depender de muitos fatores, incluindo a qualidade "
        "da implementação de cada árvore, as características do conjunto de dados (ex: dados já ordenados, "
        "aleatórios, etc.), e o ambiente de execução. Para operações de busca intensiva, a AVL ainda é "
        "frequentemente preferida teoricamente devido à sua menor altura garantida. Para cenários com "
        "muitas inserções e remoções, a Rubro-Negra muitas vezes leva vantagem."
    )
    story.append(Paragraph(texto_consideracoes, styles['CorpoTexto']))

    # 5. Conclusão
    story.append(Paragraph("5. Conclusão", styles['CabecalhoSecao']))
    texto_conclusao = (
        f"O experimento demonstrou que para a operação de inserção em massa do conjunto de dados "
        f"<code>dados100_mil.txt</code>:<br/>"
        f"&nbsp;&nbsp;&nbsp;&nbsp;&bull; A Árvore Rubro-Negra levou <b>{TEMPO_RB_MS} ms</b> e realizou <b>{NUMERO_COMPARACOES_RB}</b> comparações.<br/>"
        f"&nbsp;&nbsp;&nbsp;&nbsp;&bull; A Árvore AVL levou <b>{TEMPO_AVL_MS} ms</b> e realizou <b>{NUMERO_COMPARACOES_AVL}</b> comparações.<br/><br/>"
        f"Ambas as estruturas oferecem desempenho logarítmico garantido, mas as diferenças em suas "
        f"estratégias de balanceamento podem levar a variações de desempenho prático dependendo da "
        f"operação predominante e da natureza dos dados. "
        f"Neste caso específico de inserção em massa, {'a Árvore Rubro-Negra' if (TEMPO_RB_MS.isdigit() and TEMPO_AVL_MS.isdigit() and int(TEMPO_RB_MS) < int(TEMPO_AVL_MS)) else ('a Árvore AVL' if (TEMPO_RB_MS.isdigit() and TEMPO_AVL_MS.isdigit() and int(TEMPO_AVL_MS) < int(TEMPO_RB_MS)) else 'ambas as árvores')} "
        f"apresentou{' (ou apresentaram)' if not (TEMPO_RB_MS.isdigit() and TEMPO_AVL_MS.isdigit() and TEMPO_RB_MS != TEMPO_AVL_MS) else ''} "
        f"um desempenho {'mais eficiente.' if (TEMPO_RB_MS.isdigit() and TEMPO_AVL_MS.isdigit() and int(TEMPO_RB_MS) < int(TEMPO_AVL_MS)) or (TEMPO_RB_MS.isdigit() and TEMPO_AVL_MS.isdigit() and int(TEMPO_AVL_MS) < int(TEMPO_RB_MS)) else 'comparável.'}"
    )
    story.append(Paragraph(texto_conclusao, styles['CorpoTexto']))
    story.append(Paragraph(f"<i>Observação:</i> Os tempos de execução podem variar a cada execução devido a fatores como carga do sistema, cache, e outros processos em execução no computador. Na última execução realizada em {__import__('datetime').datetime.now().strftime('%d/%m/%Y, %H:%M')}, os tempos observados foram: Rubro-Negra = {TEMPO_RB_MS} ms, AVL = {TEMPO_AVL_MS} ms.", styles['CorpoTexto']))
    
    try:
        doc.build(story)
        print(f"PDF '{nome_arquivo_pdf}' gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao gerar o PDF: {e}")

if __name__ == '__main__':
    gerar_pdf_relatorio()
