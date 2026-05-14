import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregamento e Limpeza
df = pd.read_excel("compras.xlsx", skiprows=2)
df = df.dropna(how="all", axis=1).dropna(how="all").reset_index(drop=True)

# 2. Identificação Dinâmica de Colunas
# Isso ajuda se o nome da coluna mudar levemente (ex: "VALOR TOTAL" ou "Valor")
col_valor = next((c for c in df.columns if 'VALOR' in c.upper()), None)
col_fornecedor = next((c for c in df.columns if 'FORNECEDOR' in c.upper()), None)

if col_valor:
    df[col_valor] = pd.to_numeric(df[col_valor], errors='coerce')
    total_geral = df[col_valor].sum()
    print(f"💰 Total Geral: R$ {total_geral:.2f}")

# 3. Agrupamento e Relatório
if col_fornecedor and col_valor:
    resumo = df.groupby(col_fornecedor)[col_valor].sum().sort_values(ascending=False)
    
    # Exportação para Excel com múltiplas abas
    with pd.ExcelWriter("relatorio_final.xlsx") as writer:
        df.to_excel(writer, sheet_name="Dados Limpos", index=False)
        resumo.to_excel(writer, sheet_name="Resumo por Fornecedor")
    
    print("\n✅ Relatório exportado: relatorio_final.xlsx")

    # 4. Visualização
    resumo.plot(kind="bar", title="Gasto por Fornecedor", color='#8b5cf6')
    plt.tight_layout()
    plt.show()
