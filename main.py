import pandas as pd
import matplotlib.pyplot as plt
import os

def executar_automacao():
    arquivo_entrada = "compras.xlsx"
    arquivo_saida = "relatorio_final.xlsx"
    
    if not os.path.exists(arquivo_entrada):
        print(f"❌ Erro: O arquivo {arquivo_entrada} não foi encontrado!")
        return

    print("🚀 Localizando cabeçalhos...")
    
    # 1. Busca dinâmica da linha do cabeçalho
    df_busca = pd.read_excel(arquivo_entrada, header=None)
    linha_cabecalho = None
    for i, row in df_busca.iterrows():
        if "FORNECEDOR" in row.values:
            linha_cabecalho = i
            break
    
    if linha_cabecalho is None:
        print("❌ Erro: Não encontrei a coluna 'FORNECEDOR'.")
        return

    # 2. Leitura e Limpeza
    df = pd.read_excel(arquivo_entrada, skiprows=linha_cabecalho)
    df.columns = [str(c).strip().replace('\n', ' ') for c in df.columns]

    col_fornecedor = "FORNECEDOR"
    col_valor = "VALOR NOTA"

    if col_fornecedor in df.columns and col_valor in df.columns:
        df[col_valor] = pd.to_numeric(df[col_valor], errors='coerce')
        df = df.dropna(subset=[col_fornecedor, col_valor])
        df = df[df[col_fornecedor] != "MERCADO LIVRE"]

        # 3. Agrupamento (O Insight)
        resumo = df.groupby(col_fornecedor)[col_valor].sum().sort_values(ascending=False)

        # --- MELHORIA SÊNIOR: ESTILIZAÇÃO ---
        def destacar_gastos_altos(s):
            ''' Pinta de vermelho células com valor acima de 5000 '''
            return ['background-color: #f87171; color: white; font-weight: bold' if v > 5000 else '' for v in s]

        # --- MELHORIA SÊNIOR: TRATAMENTO DE ERRO DE PERMISSÃO ---
        try:
            with pd.ExcelWriter(arquivo_saida, engine='openpyxl') as writer:
                # Salva aba principal
                df.to_excel(writer, sheet_name="Dados Tratados", index=False)
                
                # Salva aba de resumo com a formatação condicional
                resumo_estilizado = resumo.to_frame().style.apply(destacar_gastos_altos, subset=[col_valor])
                resumo_estilizado.to_excel(writer, sheet_name="Resumo por Fornecedor")
            
            print(f"✅ Relatório '{arquivo_saida}' gerado com sucessso!")
            
            # 4. Geração do Gráfico (Visual)
            plt.figure(figsize=(12, 6))
            resumo.head(10).plot(kind="bar", color='#8b5cf6')
            plt.title("Top 10 Gastos por Fornecedor")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig("grafico_resultado.png")
            print("📊 Gráfico atualizado: grafico_resultado.png")
            plt.show()

        except PermissionError:
            print("\n" + "!"*60)
            print("❌ ERRO DE ACESSO AO ARQUIVO:")
            print(f"O arquivo '{arquivo_saida}' está aberto no seu Excel.")
            print("Por favor, FECHE O EXCEL e tente rodar o script novamente.")
            print("!"*60 + "\n")
            
    else:
        print("❌ Colunas não encontradas.")

if __name__ == "__main__":
    executar_automacao()