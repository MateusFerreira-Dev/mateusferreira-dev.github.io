import pandas as pd

# Ler Excel
df = pd.read_excel("compras.xlsx", skiprows=3)

# Limpeza
df = df.dropna(how="all", axis=1)
df = df.dropna(how="all")

df.columns = df.iloc[0]
df = df[1:]

# Resetar índice
df = df.reset_index(drop=True)

print("DADOS TRATADOS:")
print(df.head())

# -------------------------
# 💰 TOTAL
# -------------------------
col_valor = None

for col in df.columns:
    if "valor" in str(col).lower():
        col_valor = col

if col_valor:
    df[col_valor] = pd.to_numeric(df[col_valor], errors='coerce')
    total = df[col_valor].sum()

    print("\n💰 Total geral:", total)

# -------------------------
# 📊 AGRUPAR (se tiver fornecedor)
# -------------------------
col_fornecedor = None

for col in df.columns:
    if "fornecedor" in str(col).lower():
        col_fornecedor = col

if col_fornecedor and col_valor:
    resumo = df.groupby(col_fornecedor)[col_valor].sum().sort_values(ascending=False)

    print("\n📊 Total por fornecedor:")
    print(resumo)

# -------------------------
# 📁 EXPORTAR NOVO EXCEL
# -------------------------
with pd.ExcelWriter("relatorio_final.xlsx") as writer:
    df.to_excel(writer, sheet_name="Dados Limpos", index=False)

    if col_fornecedor and col_valor:
        resumo.to_excel(writer, sheet_name="Resumo por Fornecedor")

print("\n✅ Relatório exportado como: relatorio_final.xlsx")

# -------------------------
# 📈 GRÁFICO
# -------------------------
if col_fornecedor and col_valor:
    resumo.plot(kind="bar", title="Total por Fornecedor")
    
    import matplotlib.pyplot as plt
    plt.show()
