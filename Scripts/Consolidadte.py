import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo Excel
file_path = "C:\\Users\\Admin\\Documents\\DIO\\Utilizando prompts para gerar insights de relatorios de vendas\\Projeto Base\\Data\\processed_data\\Meganium.xlsx"  # Substitua pelo caminho correto do seu arquivo
df = pd.read_excel(file_path, sheet_name="Cosolidate")

# Criar resumo das vendas por país
summary = df.groupby("delivery_country").agg(
    total_sales=("invoice_id", "count"),       # Contagem de pedidos
    total_quantity=("quantity", "sum"),        # Quantidade total vendida
    total_revenue=("total_price", "sum"),      # Receita total
    avg_order_value=("total_price", "mean")    # Ticket médio por pedido
).reset_index()

# Ordenar pelo total de vendas
summary = summary.sort_values(by="total_sales", ascending=False)

# Salvar o resumo em CSV
csv_output_path = "resumo_vendas_por_pais.csv"
summary.to_csv(csv_output_path, index=False)
print(f"Resumo de vendas salvo em: {csv_output_path}")

# Encontrar o produto mais vendido por país
top_products = df.groupby(["delivery_country", "product_sold"])["quantity"].sum().reset_index()
top_products = top_products.loc[top_products.groupby("delivery_country")["quantity"].idxmax()]

# Criar gráfico
plt.figure(figsize=(12, 6))
sns.barplot(x="delivery_country", y="quantity", hue="product_sold", data=top_products, palette="viridis")
plt.xlabel("País")
plt.ylabel("Quantidade Vendida")
plt.title("Produto Mais Vendido por País")
plt.legend(title="Produto")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar gráfico
plt.savefig("grafico_produto_mais_vendido.png")
plt.show()

print("Gráfico salvo como 'grafico_produto_mais_vendido.png'.")
