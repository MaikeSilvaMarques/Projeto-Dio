import pandas as pd

# 📂 Substitua pelo caminho correto do seu arquivo Excel
file_path = r"C:\\Users\\Admin\\Documents\\DIO\\Utilizando prompts para gerar insights de relatorios de vendas\\Projeto Base\\Data\\processed_data\\Meganium.xlsx"

# 🔹 Carregar os dados da planilha "Cosolidate"
df = pd.read_excel(file_path, sheet_name="Cosolidate")

# 🔹 Agrupar por país e produto para calcular quantidade vendida e receita total
sales_summary = df.groupby(["delivery_country", "product_sold"]).agg(
    total_quantity=("quantity", "sum"),        # Quantidade total vendida
    total_revenue=("total_price", "sum")      # Receita total por produto
).reset_index()

# 🔹 Encontrar o produto mais vendido por país (maior quantidade)
top_products = sales_summary.loc[sales_summary.groupby("delivery_country")["total_quantity"].idxmax()]

# 🔹 Salvar o resumo em CSV
csv_output_path = "resumo_produtos_mais_vendidos_por_pais.csv"
top_products.to_csv(csv_output_path, index=False)

print(f"Resumo salvo em: {csv_output_path}")
